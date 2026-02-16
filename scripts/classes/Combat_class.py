import pygame
import random
import time
from enum import Enum  # For simple combat state management (IDLE/BUSY)

from scripts.classes.SoundControl_class import sound_control
from scripts.logic.assets_management import load_image, load_font
from scripts.classes.Pokedex_class import easy_pokedex
from scripts.classes.PokemonDisplay_class import PokemonDisplay
from scripts.logic.json_management import save_pokemons_to_json
from scripts.classes.ConfirmationBox_class import ConfirmationBox

class CombatState(Enum):
    IDLE = 0  # No action in progress, player can choose an action
    BUSY = 1  # An action/animation is in progress, inputs should be ignored

class Combat:
    def __init__(self, pokedex):
        """
        Combat system between the player's Pokémon and a random wild Pokémon.
        :param pokedex: The player's Pokedex (contains their Pokémon)
        """

        self.__player_pokedex = pokedex
        self.__player_pokemon = pokedex.get_pokemons()[0]  # TEMP: first Pokémon
        self.__adversary = self.generate_random_adversary()
        self.ko_winner = None

        # Background
        self.background = load_image("assets/images/forest_background.jpg")
        self.background = pygame.transform.scale(self.background, (800,600))

        # UI fonts
        self.font = load_font("assets/font/Pokemon_GB.ttf", 20)

        # Combat state
        self.running = True

        # Combat flow state
        self.state = CombatState.IDLE  # Current combat state (IDLE or BUSY)

        # Simple timing system for delayed actions/animations
        self.animation_timer = None    # Stores the time when current animation/action should finish
        self.animation_callback = None # Function to call when the timer is reached

        # UI buttons
        self.button_attack = pygame.Rect(40, 200, 200, 50)  # Attack button area
        self.button_heal   = pygame.Rect(300, 200, 200, 50) # Heal button area
        self.button_run    = pygame.Rect(560, 200, 200, 50) # Run button area

        self.dialog_box = ConfirmationBox(self.font)  # Handles centered messages and click-to-continue

    def is_busy(self):
        """ Returns True if combat is currently processing an action/animation """
        return self.state == CombatState.BUSY
    def set_idle_state(self):
        """ Set combat back to IDLE state after dialog """
        self.state = CombatState.IDLE

    def draw_buttons(self, screen):
        """ Draw simple Combat UI buttons """

        # Attack button
        pygame.draw.rect(screen, (255, 255, 255), self.button_attack)
        text = self.font.render("ATTACK", True, (0, 0, 0))
        screen.blit(text, (self.button_attack.x + 40, self.button_attack.y + 10))

        # Heal button
        pygame.draw.rect(screen, (255, 255, 255), self.button_heal)
        text = self.font.render("HEAL", True, (0, 0, 0))
        screen.blit(text, (self.button_heal.x + 60, self.button_heal.y + 10))

        # Run button
        pygame.draw.rect(screen, (255, 255, 255), self.button_run)
        text = self.font.render("RUN", True, (0, 0, 0))
        screen.blit(text, (self.button_run.x + 70, self.button_run.y + 10))

    def handle_mouse_click(self, pos):
        """ Gets player action from button click """
        # Ignore clicks if combat is busy
        if self.state == CombatState.BUSY:
            return

        # Check which button was clicked
        if self.button_attack.collidepoint(pos):
            self.start_action("ATTACK")  # Player clicked ATTACK

        elif self.button_heal.collidepoint(pos):
            self.start_action("HEAL")    # Player clicked HEAL

        elif self.button_run.collidepoint(pos):
            self.start_action("RUN")     # Player clicked RUN

    def play_animation(self, name, callback):
        # Set a simple non-blocking timer for the action/animation

        durations = {
            "ATTACK": 400,  # milliseconds
            "HEAL":   400,
            "RUN":    300
        }

        self.animation_timer = pygame.time.get_ticks() + durations.get(name, 300)
        self.animation_callback = callback
        self.state = CombatState.BUSY  # Block inputs while waiting

    def start_action(self, action_type):
        # Entry point when player clicks a button

        if self.is_busy():
            return  # Ignore if combat is already processing something

        if action_type == "ATTACK":
            self.play_animation("ATTACK", self.resolve_attack)

        elif action_type == "HEAL":
            self.play_animation("HEAL", self.resolve_heal)

        elif action_type == "RUN":
            self.play_animation("RUN", self.resolve_run)

    def resolve_attack(self):
        # Player attacks first
        self.player_attack()
        result = self.check_end()

        if result == "enemy_ko":
            # Enemy is KO, play KO animation and show message
            self.ko_winner = "player"
            # We need displays from run(), so we will set them as attributes there
            self.adversary_display.start_ko_animation()

            # Show dialog, then finalize battle when closed
            self.dialog_box.show(
                (800, 600),
                f"{self.__adversary.get_name()} fainted!",
                callback=lambda: self.finalize_battle("player")
            )
            return

        # Enemy attacks if still alive
        self.enemy_attack()
        result = self.check_end()

        if result == "player_ko":
            self.ko_winner = "enemy"
            self.player_display.start_ko_animation()

            self.dialog_box.show(
                (800, 600),
                f"{self.__player_pokemon.get_name()} fainted!",
                callback=lambda: self.finalize_battle("enemy")
            )
            return

        # No KO: show a simple message and return to IDLE after dialog
        self.dialog_box.show(
            (800, 600),
            f"{self.__player_pokemon.get_name()} attacked!",
            callback=self.set_idle_state
        )

    def resolve_heal(self):
        # Heal 60% of max HP
        p = self.__player_pokemon
        heal_amount = int(p.get_max_hp() * 0.6)
        p.set_hp(min(p.get_max_hp(), p.get_hp() + heal_amount))

        # Enemy attacks after heal
        self.enemy_attack()
        result = self.check_end()

        if result == "player_ko":
            self.ko_winner = "enemy"
            self.player_display.start_ko_animation()

            self.dialog_box.show(
                (800, 600),
                f"{self.__player_pokemon.get_name()} fainted!",
                callback=lambda: self.finalize_battle("enemy")
            )
            return

        # Show heal message and go back to IDLE after dialog
        self.dialog_box.show(
            (800, 600),
            f"{p.get_name()} healed!",
            callback=self.set_idle_state
        )
    
    def resolve_run(self):
        # Player runs away, end combat immediately

        self.dialog_box.show(
            (800, 600),
            "You ran away safely.",
            callback=lambda: self.finalize_battle("player")  # Or special 'run' result if you prefer
        )

    def generate_random_adversary(self):
        """Creates a random wild Pokémon for the encounter."""
        return random.choice(easy_pokedex.get_pokemons())

    def apply_types(self, attacker_types, defender_types):
        """Define attacker's types efficiency against defender."""
        efficiency = 1
        for attype in attacker_types:
            for deftype in defender_types:
                if deftype in attype.get_weaknesses():
                    efficiency *= 0.5
                if deftype in attype.get_strenghts():
                    efficiency *= 2
                if deftype in attype.get_useless():
                    efficiency *= 0
        return efficiency

    def compute_damage(self, attacker, defender):
        """Pokémon-like damage formula."""
        damage = (((2 * attacker.get_level() / 5) * (attacker.get_attack() / defender.get_defense())) / 25 + 10) * 1.5 * self.apply_types(attacker.get_types(), defender.get_types()) * (random.randint(60,100) / 100)
        return int(max(1, damage))

    def draw_pokemon_stats(self, screen):
        """Draws HP bars and names."""
        # Player
        p = self.__player_pokemon
        text = self.font.render(f"{p.get_name()}  HP: {p.get_hp()}", True, (255, 255, 255))
        screen.blit(text, (40, 350))

        # Enemy
        e = self.__adversary
        text2 = self.font.render(f"{e.get_name()}  HP: {e.get_hp()}", True, (255, 255, 255))
        screen.blit(text2, (400, 40))

    #  ATTACKS
    def player_attack(self):
        dmg = self.compute_damage(self.__player_pokemon, self.__adversary)
        self.__adversary.set_hp(self.__adversary.get_hp() - dmg)
        print(f"{self.__player_pokemon.get_name()} dealt {dmg} damage!")

    def enemy_attack(self):
        dmg = self.compute_damage(self.__adversary, self.__player_pokemon)
        self.__player_pokemon.set_hp(self.__player_pokemon.get_hp() - dmg)

    # End conditions
    def check_end(self):
        if self.__adversary.get_hp() <= 0:
            return "enemy_ko"

        if self.__player_pokemon.get_hp() <= 0:
            return "player_ko"

        return None
    
    def finalize_battle(self, winner):
        
    # Play victory music and reward the player if they won
        if winner == "player":
            sound_control.play_music("assets/music/victory.mp3")

            # Add the defeated Pokémon to the player's Pokédex
            self.__player_pokedex.add_pokemon(self.__adversary)

            # Restore HP of both Pokémon after the battle
            self.__player_pokemon.set_hp(self.__player_pokemon.get_max_hp())
            self.__adversary.set_hp(self.__adversary.get_max_hp())

            # Save updated Pokédex to JSON file
            save_pokemons_to_json(
                self.__player_pokedex.get_pokemons(),
                "assets/data/player_pokemons.json"
            )

        else:
            # Player lost: simply restore HP of both Pokémon
            self.__player_pokemon.set_hp(self.__player_pokemon.get_max_hp())
            self.__adversary.set_hp(self.__adversary.get_max_hp())

        # Stop the combat loop
        self.running = False

    #  Main combat loop
    def run(self, screen, clock):
        """Main combat loop."""

        # Initialize Pokémon sprite displays
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
                    self.animation_callback()
                    self.animation_callback = None

            # Handle ongoing animations (entry or KO)
            if player_display.current_animation or adversary_display.current_animation:
                player_display.update()
                adversary_display.update()

                screen.blit(self.background, (0, 0))
                self.draw_pokemon_stats(screen)
                player_display.draw(screen)
                adversary_display.draw(screen)

                pygame.display.flip()
                clock.tick(60)

                # If a KO happened and all animations are finished, end the battle
                if self.ko_winner and not player_display.current_animation and not adversary_display.current_animation:
                    self.finalize_battle(self.ko_winner)

                continue

            # Handle player input (turn-based combat)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                # If a dialog box is active, clicks are for it only
                if self.dialog_box.active:
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        self.dialog_box.handle_click(mouse_pos)
                    continue  # Skip normal input when dialog is active

                # Mouse click detection for combat buttons
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    self.handle_mouse_click(mouse_pos)

            # Normal drawing when no animation is active
            screen.blit(self.background, (0, 0))
            self.draw_pokemon_stats(screen)

            player_display.update()
            player_display.draw(screen)
            adversary_display.update()
            adversary_display.draw(screen)

            self.draw_buttons(screen)  # Draw action buttons

            # Draw dialog box on top if active
            self.dialog_box.draw(screen)

            pygame.display.flip()
            clock.tick(60)




