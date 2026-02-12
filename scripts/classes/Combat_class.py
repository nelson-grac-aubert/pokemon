import pygame
import random
from scripts.classes.SoundControl_class import sound_control
from scripts.logic.assets_management import load_gif, load_image, load_font
from scripts.classes.Pokedex_class import Pokedex, kanto_pokedex, easy_pokedex
from scripts.classes.PokemonDisplay_class import PokemonDisplay
from scripts.classes.PokemonType_class import PokemonType
from scripts.logic.json_management import load_pokemons_from_json, load_types_from_json, save_pokemons_to_json

class Combat:
    def __init__(self, pokedex):
        """
        Combat system between the player's Pokémon and a random wild Pokémon.
        :param pokedex: The player's Pokedex (contains their Pokémon)
        """

        self.__player_pokedex = pokedex
        self.__player_pokemon = pokedex.get_pokemons()[0]  # TEMP: first Pokémon
        self.__adversary = self.generate_random_adversary()

        # Background
        self.background = load_image("assets/images/forest_background.jpg")
        self.background = pygame.transform.scale(self.background, (800,600))

        # UI fonts
        self.font = load_font("assets/font/Pokemon_GB.ttf", 20)

        # Combat state
        self.running = True

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

    #  Main combat loop
    def run(self, screen, clock):
        """Main combat loop."""

        player_display = PokemonDisplay(self.__player_pokemon, 4, False)
        player_display.set_position(200,520)
        adversary_display = PokemonDisplay(self.__adversary, 3, True)
        adversary_display.set_position(600,435)

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Player attacks when pressing SPACE
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.player_attack()
                    if self.check_end():
                        break

                    self.enemy_attack()
                    self.check_end()

            # Draw
            screen.blit(self.background, (0, 0))
            self.draw_pokemon_stats(screen)

            # Animate pokemons sprites
            player_display.update()
            player_display.draw(screen)
            adversary_display.update()
            adversary_display.draw(screen)

            pygame.display.flip()
            clock.tick(60)

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
            sound_control.play_music("assets/music/victory.mp3")

            # Add vanquished Pokémon to Player Pokédex
            self.__player_pokedex.add_pokemon(self.__adversary)

            # Fully heal both Pokémons
            self.__player_pokemon.set_hp(self.__player_pokemon.get_max_hp())
            self.__adversary.set_hp(self.__adversary.get_max_hp())

            # Save
            save_pokemons_to_json(self.__player_pokedex.get_pokemons(), "assets/data/player_pokemons.json")

            self.running = False
            return True

        if self.__player_pokemon.get_hp() <= 0:

            # Fully heal both Pokémons
            self.__player_pokemon.set_hp(self.__player_pokemon.get_max_hp())
            self.__adversary.set_hp(self.__adversary.get_max_hp())
            
            self.running = False
            return True

        return False