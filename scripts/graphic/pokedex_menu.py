import pygame
from scripts.classes.Pokedex_class import Pokedex
from scripts.classes.PokedexDisplay_class import PokedexDisplay
from scripts.classes.PlayerPokedex_class import PlayerPokedex
from scripts.classes.PlayerPokedexDisplay_class import PlayerPokedexDisplay

def run_pokedex(player_pokedex):
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pokédex")

    # Auto-select correct display class
    if isinstance(player_pokedex, PlayerPokedex):
        pokedex_display = PlayerPokedexDisplay(player_pokedex, screen)
    else:
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

        if pokedex_display.request_exit:
            return

    pygame.quit()