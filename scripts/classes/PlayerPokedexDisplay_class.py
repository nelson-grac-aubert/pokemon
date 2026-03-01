import pygame
from scripts.classes.PokedexDisplay_class import PokedexDisplay
from scripts.classes.DialogBox import DialogBox

class PlayerPokedexDisplay(PokedexDisplay):

    def __init__(self, pokedex, screen):
        super().__init__(pokedex, screen)

        # Registered button
        bx = self.back_button_rect.x
        by = self.back_button_rect.y - 60
        bw = self.back_button_rect.width
        bh = self.back_button_rect.height
        self.registered_button_rect = pygame.Rect(bx, by, bw, bh)

        # Action buttons
        base_x = self.left_width + 20
        base_y = screen.get_height() - 120
        w, h = 220, 40

        self.choose_button_rect = pygame.Rect(base_x, base_y, w, h)
        self.abandon_button_rect = pygame.Rect(base_x, base_y + 60, w, h)

        self.action_button_color = (255, 150, 170)

        # Dialog
        self.dialog = DialogBox(screen, self.font)

    def draw_right_panel(self):
        super().draw_right_panel()

        # Registered button
        pygame.draw.rect(self.screen, (200, 50, 50), self.registered_button_rect)
        reg_txt = self.font.render("Pokédex", True, (255, 255, 255))
        self.screen.blit(reg_txt, reg_txt.get_rect(center=self.registered_button_rect.center))

        # Choose
        pygame.draw.rect(self.screen, self.action_button_color, self.choose_button_rect)
        choose_txt = self.font.render("Choose", True, (0, 0, 0))
        self.screen.blit(choose_txt, choose_txt.get_rect(center=self.choose_button_rect.center))

        # Abandon
        pygame.draw.rect(self.screen, self.action_button_color, self.abandon_button_rect)
        abandon_txt = self.font.render("Abandon", True, (0, 0, 0))
        self.screen.blit(abandon_txt, abandon_txt.get_rect(center=self.abandon_button_rect.center))

        self.dialog.draw()

    def handle_event(self, event):
        if self.dialog.is_open():
            self.dialog.handle_event(event)
            return

        super().handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos

            pokemons = self.get_pokedex().get_pokemons()
            if not pokemons:
                return

            current_pokemon = pokemons[self.selected_index]

            # Choose
            if self.choose_button_rect.collidepoint(mx, my):
                self.get_pokedex().choose_as_combat_pokemon(current_pokemon)
                self.dialog.show(f"{current_pokemon.get_name()} has been chosen as your combat Pokémon!")
                return

            # Abandon
            if self.abandon_button_rect.collidepoint(mx, my):

                if len(pokemons) <= 1:
                    self.dialog.show("You cannot abandon your only Pokémon!")
                    return

                if self.get_pokedex().combat_pokemon is current_pokemon:
                    self.dialog.show("You cannot abandon your combat Pokémon! Swap it first.")
                    return

                self.get_pokedex().abandon_pokemon(current_pokemon)

                if self.selected_index >= len(self.get_pokedex().get_pokemons()):
                    self.selected_index = max(0, len(self.get_pokedex().get_pokemons()) - 1)

                self.load_current_pokemon_display()
                return