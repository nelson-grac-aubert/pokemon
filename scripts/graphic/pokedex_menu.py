import pygame
from scripts.classes.Pokedex_class import Pokedex
from scripts.classes.PokedexDisplay_class import PokedexDisplay
from scripts.logic.json_management import load_pokemons_from_json, load_types_from_json

def run_pokedex():
    pygame.init()

    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Pokédex")

    pokedex = Pokedex()
    pokedex.set_pokemons(load_pokemons_from_json("assets/data/all_pokemons.json", 
                        load_types_from_json("assets/data/all_types.json")))

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