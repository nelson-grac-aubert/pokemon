import pygame
from scripts.classes.Pokedex_class import Pokedex
from scripts.classes.PokedexDisplay_class import PokedexDisplay
from scripts.logic.json_management import load_pokemons_from_json, load_types_from_json

def run_pokedex(player_pokedex):
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pokédex")

    # Use the player's current Pokédex instead of loading the full one
    pokedex_display = PokedexDisplay(player_pokedex, screen)

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

        # Back to overworld
        if pokedex_display.request_exit:
            return

    pygame.quit()