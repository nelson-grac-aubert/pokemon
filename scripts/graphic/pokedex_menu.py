import pygame
from scripts.classes.Pokedex_class import Pokedex
from scripts.classes.PokedexDisplay_class import PokedexDisplay
from scripts.data.all_pokemons import kanto_pokemons

def run_pokedex():
    pygame.init()

    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Pokédex")

    pokedex = Pokedex()
    pokedex.set_pokemons(kanto_pokemons)

    pokedex_display = PokedexDisplay(pokedex, screen)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            pokedex_display.handle_event(event)

        screen.fill((0, 0, 0))
        pokedex_display.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()