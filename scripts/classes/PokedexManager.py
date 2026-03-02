import pygame

class PokedexManager:

    def __init__(self, screen, player_pokedex, registered_pokedex):
        self.screen = screen
        self.player_pokedex = player_pokedex
        self.registered_pokedex = registered_pokedex

        self.current_display = None
        self.open_registered()

    def open_pc(self):
        from scripts.classes.PlayerPokedexDisplay import PlayerPokedexDisplay
        self.current_display = PlayerPokedexDisplay(self.player_pokedex, self.screen)

    def open_registered(self):
        from scripts.classes.RegisteredPokedexDisplay import RegisteredPokedexDisplay
        self.current_display = RegisteredPokedexDisplay(self.registered_pokedex, self.screen)

    def update(self, events):
        if not self.current_display:
            return

        self.current_display.draw()

        for event in events:
            self.current_display.handle_event(event)

            # Exit
            if self.current_display.request_exit:
                self.current_display = None
                return

            # Registered → PC
            if hasattr(self.current_display, "request_pc_switch"):
                if self.current_display.request_pc_switch:
                    self.open_pc()
                    return

            # PC → Registered
            if hasattr(self.current_display, "registered_button_rect"):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.current_display.registered_button_rect.collidepoint(event.pos):
                        self.open_registered()
                        return