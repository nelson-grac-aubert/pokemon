import pygame
from Pokemon_class import Pokemon
from Pokedex_class import Pokedex
from PokedexDisplay_class import PokedexDisplay
from all_pokemons import kanto_pokemons

pygame.init()

# Création du pokédex
kanto_pokedex = Pokedex()
kanto_pokedex.set_pokemons(kanto_pokemons)

# Fenêtre
screen = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Pokédex")

# Affichage pokédex
pokedex_display = PokedexDisplay(kanto_pokedex, screen)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Le pokédex gère les inputs
        pokedex_display.handle_event(event)

    # Dessin
    screen.fill((0, 0, 0))
    pokedex_display.draw()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()