import pygame
from scripts.classes.Pokedex_class import Pokedex
from scripts.classes.PokedexDisplay_class import PokedexDisplay
from scripts.classes.PlayerPokedex_class import PlayerPokedex
from scripts.classes.PlayerPokedexDisplay_class import PlayerPokedexDisplay
from scripts.classes.RegisteredPokedex import RegisteredPokedex
from scripts.classes.PokedexManager import PokedexManager

def run_pokedex(player_pokedex):
    screen = pygame.display.get_surface()
    clock = pygame.time.Clock()

    registered_pokedex = RegisteredPokedex()
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
