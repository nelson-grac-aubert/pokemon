import pygame
import random
import copy
from enum import Enum
from scripts.classes.SoundControl_class import sound_control
from scripts.logic.assets_management import load_image, load_font
from scripts.classes.Pokedex_class import kanto_pokedex
from scripts.classes.PokemonDisplay_class import PokemonDisplay
from scripts.logic.json_management import save_pokemons_to_json
from scripts.classes.MessageOverlay_class import MessageOverlay
from scripts.classes.DialogBox import DialogBox


class CombatState(Enum):
    IDLE = 0
    BUSY = 1


class Combat:
    def __init__(self, pokedex):

        self.__player_pokedex = pokedex
        self.__player_pokemon = pokedex.combat_pokemon
        self.__adversary = self.generate_random_adversary()
        self.ko_winner = None

        self.background = load_image("assets/images/forest_background.jpg")
        self.background = pygame.transform.scale(self.background, (800, 600))

        self.font = load_font("assets/font/Pokemon_GB.ttf", 20)

        self.running = True
        self.state = CombatState.IDLE

        self.animation_timer = None
        self.animation_callback = None

        self.waiting_for_dialog_close = False

        self.button_attack = pygame.Rect(40, 25, 200, 50)
        self.button_heal = pygame.Rect(300, 25, 200, 50)
        self.button_run = pygame.Rect(560, 25, 200, 50)

        self.message_overlay = MessageOverlay(load_font("assets/font/Pokemon_GB.ttf", 25))
        self.dialog = DialogBox(pygame.display.get_surface(), self.font)

    def is_busy(self):
        return self.state == CombatState.BUSY

    def set_idle_state(self):
        self.state = CombatState.IDLE

    def draw_buttons(self, screen):

        pygame.draw.rect(screen, (255, 255, 255), self.button_attack)
        text = self.font.render("ATTACK", True, (0, 0, 0))
        screen.blit(text, (self.button_attack.x + 40, self.button_attack.y + 10))

        pygame.draw.rect(screen, (255, 255, 255), self.button_heal)
        text = self.font.render("HEAL", True, (0, 0, 0))
        screen.blit(text, (self.button_heal.x + 60, self.button_heal.y + 10))

        pygame.draw.rect(screen, (255, 255, 255), self.button_run)
        text = self.font.render("RUN", True, (0, 0, 0))
        screen.blit(text, (self.button_run.x + 70, self.button_run.y + 10))

    def handle_mouse_click(self, pos):

        if self.state == CombatState.BUSY:
            return

        if self.button_attack.collidepoint(pos):
            self.start_action("ATTACK")
        elif self.button_heal.collidepoint(pos):
            self.start_action("HEAL")
        elif self.button_run.collidepoint(pos):
            self.start_action("RUN")

    def play_animation(self, name, callback):

        durations = {
            "ATTACK": 300,
            "HEAL": 300,
            "RUN": 300,
            "ENEMY_ATTACK_DELAY": 2500,
            "RUN_DELAY": 2000
        }

        self.animation_timer = pygame.time.get_ticks() + durations.get(name, 300)
        self.animation_callback = callback
        self.state = CombatState.BUSY

    def start_action(self, action_type):

        if self.is_busy():
            return

        if action_type == "ATTACK":
            self.play_animation("ATTACK", self.resolve_attack)

        elif action_type == "HEAL":
            self.play_animation("HEAL", self.resolve_heal)

        elif action_type == "RUN":
            self.play_animation("RUN", self.resolve_run)

    def resolve_attack(self):
        dmg, eff_msg = self.compute_damage(self.__player_pokemon, self.__adversary)
        self.__adversary.set_hp(self.__adversary.get_hp() - int(dmg*1.4+5))

        self.message_overlay.show(f"{self.__player_pokemon.get_name()} dealt {int(dmg*1.4+5)} dmg!" if not eff_msg else f"{self.__player_pokemon.get_name()} dealt {dmg} dmg!" + eff_msg)

        result = self.check_end()
        if result == "enemy_ko":
            self.ko_winner = "player"
            self.adversary_display.start_ko_animation()
            return

        self.play_animation("ENEMY_ATTACK_DELAY", self.enemy_turn)

    def resolve_heal(self):
        p = self.__player_pokemon
        heal_amount = int(p.get_max_hp() * 0.7)
        p.set_hp(min(p.get_max_hp(), p.get_hp() + heal_amount))

        self.message_overlay.show(f"{p.get_name()} healed {heal_amount} HP!")

        self.play_animation("ENEMY_ATTACK_DELAY", self.enemy_turn)

    def resolve_run(self):
        self.message_overlay.show("You ran away safely...")
        self.play_animation("RUN_DELAY", lambda: self.finalize_battle("enemy"))

    def enemy_turn(self):
        dmg, eff_msg = self.compute_damage(self.__adversary, self.__player_pokemon)
        self.__player_pokemon.set_hp(self.__player_pokemon.get_hp() - int(dmg*0.8))

        msg = f"{self.__adversary.get_name()} dealt {int(dmg*0.8)} dmg!"
        if eff_msg:
            msg += f"{eff_msg}"
        self.message_overlay.show(msg)

        result = self.check_end()
        if result == "player_ko":
            self.ko_winner = "enemy"
            self.player_display.start_ko_animation()
            return

        self.set_idle_state()

    def generate_random_adversary(self):
        return random.choice(kanto_pokedex.get_pokemons())

    def apply_types(self, attacker_types, defender_types):
        efficiency = 1
        message = ""

        for attype in attacker_types:
            for deftype in defender_types:
                if deftype.get_name() in [t.get_name() for t in attype.get_useless()]:
                    efficiency *= 0
                elif deftype.get_name() in [t.get_name() for t in attype.get_weaknesses()]:
                    efficiency *= 0.5
                elif deftype.get_name() in [t.get_name() for t in attype.get_strenghts()]:
                    efficiency *= 2


        if efficiency == 0:
            message = "\nIt has no effect..."
        elif efficiency < 1:
            message = "\nIt's not very effective..."
        elif efficiency > 1:
            message = "\nIt's super effective!"

        return efficiency, message

    def compute_damage(self, attacker, defender):
        eff, msg = self.apply_types(attacker.get_types(), defender.get_types())

        chance = random.randint(0,100)
        if chance >= attacker.get_precision() : 
            eff = 0 
            msg = "\nThe attack missed..." 

        # Simplified calculation of the actual Pokémon games
        damage = 1.5 * (((2 * attacker.get_level() / 5) *
                  (attacker.get_attack() / defender.get_defense())) / 25 + 10)
        # Apply types
        damage *= eff
        # Add some variance
        damage *= (random.randint(60, 100) / 100)

        return int(damage), msg

    def draw_pokemon_stats(self, screen):

        p = self.__player_pokemon
        text = self.font.render(f"{p.get_name()}  HP: {p.get_hp()}/{p.get_max_hp()}", True, (255, 255, 255))
        screen.blit(text, (40, 350))

        e = self.__adversary
        text2 = self.font.render(f"{e.get_name()}  HP: {e.get_hp()}/{e.get_max_hp()}", True, (255, 255, 255))
        screen.blit(text2, (350, 280))

    def check_end(self):
        if self.__adversary.get_hp() <= 0:
            return "enemy_ko"

        if self.__player_pokemon.get_hp() <= 0:
            return "player_ko"

        return None
        
    def identify_pokemon(self) : 
        pass


    def capture_pokemon(self) : 
        captured_pokemon = copy.deepcopy(self.__adversary)
        self.__player_pokedex.add_pokemon(captured_pokemon)

        save_pokemons_to_json(self.__player_pokedex.get_pokemons(),
                                "assets/data/player_pokemons.json")

    def finalize_battle(self, winner):

        self.__player_pokemon.set_hp(self.__player_pokemon.get_max_hp())
        self.__adversary.set_hp(self.__adversary.get_max_hp())

        if winner == "player":

            # XP gain
            xp_gain = 50 + self.__adversary.get_level() * 5
            self.__player_pokemon.gain_xp(xp_gain)

            sound_control.play_music("assets/music/victory.mp3")
            self.capture_pokemon()
            self.dialog.show(f"Your {self.__player_pokemon.get_name()} wins! Enemy {self.__adversary.get_name()} has been defeated and added to the Pokédex.")
            self.state = CombatState.BUSY
            self.waiting_for_dialog_close = True
            return self.__player_pokemon.get_name()
        
        else:
            self.dialog.show(f"Enemy {self.__adversary.get_name()} wins! You took some time to heal {self.__player_pokemon.get_name()} and rest.")
            self.state = CombatState.BUSY
            self.waiting_for_dialog_close = True
            return self.__player_pokemon.get_name()
        

    def run(self, screen, clock):

        self.player_display = PokemonDisplay(self.__player_pokemon, 4, False)
        self.player_display.set_position(200, 520)
        self.player_display.start_entry_animation(from_left=True)

        self.adversary_display = PokemonDisplay(self.__adversary, 3, True)
        self.adversary_display.set_position(600, 435)
        self.adversary_display.start_entry_animation(from_left=False)

        player_display = self.player_display
        adversary_display = self.adversary_display

        while self.running:

            if self.animation_timer and pygame.time.get_ticks() >= self.animation_timer:
                self.animation_timer = None
                if self.animation_callback:
                    callback = self.animation_callback
                    self.animation_callback = None
                    callback()
                    continue

            if player_display.current_animation or adversary_display.current_animation:

                screen.blit(self.background, (0, 0))
                player_display.update()
                adversary_display.update()
                self.draw_pokemon_stats(screen)
                player_display.draw(screen)
                adversary_display.draw(screen)
                self.message_overlay.update()
                self.message_overlay.draw(screen)
                self.dialog.draw()

                pygame.display.flip()
                clock.tick(60)

                if not player_display.current_animation and not adversary_display.current_animation and self.ko_winner is None:
                    self.state = CombatState.IDLE

                if self.ko_winner and not player_display.current_animation and not adversary_display.current_animation:
                    self.finalize_battle(self.ko_winner)

                continue

            for event in pygame.event.get():

                if self.dialog.is_open():
                    self.dialog.handle_event(event)
                    continue

                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    self.handle_mouse_click(mouse_pos)

            if self.waiting_for_dialog_close:

                screen.blit(self.background, (0, 0))
                player_display.update()
                adversary_display.update()
                self.draw_pokemon_stats(screen)
                player_display.draw(screen)
                adversary_display.draw(screen)
                self.message_overlay.update()
                self.message_overlay.draw(screen)
                self.dialog.draw()

                pygame.display.flip()
                clock.tick(60)

                if not self.dialog.is_open():
                    self.running = False

                continue

            screen.blit(self.background, (0, 0))
            self.draw_pokemon_stats(screen)
            player_display.update()
            player_display.draw(screen)
            adversary_display.update()
            adversary_display.draw(screen)
            self.draw_buttons(screen)
            self.message_overlay.update()
            self.message_overlay.draw(screen)
            self.dialog.draw()

            pygame.display.flip()
            clock.tick(60)