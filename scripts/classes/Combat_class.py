import pygame
import random
from scripts.logic.assets_management import load_gif, load_image, load_font
from scripts.classes.Pokedex_class import Pokedex
from scripts.logic.json_management import load_pokemons_from_json, load_types_from_json

class Combat:
    def __init__(self, pokedex):
        """
        Combat system between the player's Pokémon and a random wild Pokémon.
        :param pokedex: The player's Pokedex (contains their Pokémon)
        """
        self.__kanto_pokedex =  Pokedex()
        self.__kanto_pokedex.set_pokemons(load_pokemons_from_json("assets/data/all_pokemons.json", load_types_from_json("assets/data/all_types.json")))
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
        return random.choice(self.__kanto_pokedex.get_pokemons())

    def compute_damage(self, attacker, defender):
        """Basic Pokémon-like damage formula."""
        base = attacker.get_attack() - defender.get_defense() // 2
        return max(1, base)

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

            pygame.display.flip()
            clock.tick(60)

    #  ATTACKS
    def player_attack(self):
        dmg = self.compute_damage(self.__player_pokemon, self.__adversary)
        self.__adversary.set_hp(self.__adversary.get_hp() - dmg)
        print(f"{self.__player_pokemon.get_name()} dealt {dmg} damage!")

    def enemy_attack(self):
        dmg = self.compute_damage(self.__adversary, self.__player_pokemon)
        self.__player_pokemon.set_hp(self.__player_pokemon.get_hp() - (dmg//10))

    # End conditions
    def check_end(self):
        if self.__adversary.get_hp() <= 0:
            print("🎉 You won the battle!")
            self.__player_pokedex.add_pokemon(self.__adversary)
            self.__player_pokemon.set_hp(100)
            self.running = False
            return True

        if self.__player_pokemon.get_hp() <= 0:
            print("💀 Your Pokémon fainted!")
            self.__player_pokemon.set_hp(100)
            self.running = False
            return True

        return False