import pygame
from scripts.classes.PokedexManager import PokedexManager

def run_pokedex(player_pokedex, registered_pokedex):
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    # Use the registered pokedex passed by the overworld
    manager = PokedexManager(screen, player_pokedex, registered_pokedex)

    running = True
    while running:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

        manager.update(events)

        if manager.current_display is None:
            running = False

        pygame.display.flip()
        clock.tick(60)