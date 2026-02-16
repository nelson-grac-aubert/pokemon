import pygame
from scripts.classes.PokedexDisplay_class import PokedexDisplay

class PlayerPokedexDisplay(PokedexDisplay):

    def __init__(self, pokedex, screen):
        super().__init__(pokedex, screen)

        # Action buttons (bottom-left of the right panel)
        base_x = self.left_width + 20
        base_y = screen.get_height() - 120
        w, h = 220, 40

        self.choose_button_rect = pygame.Rect(base_x, base_y, w, h)
        self.abandon_button_rect = pygame.Rect(base_x, base_y + 60, w, h)

        # Light pink button color
        self.action_button_color = (255, 150, 170)

        # Dialog message (None = no dialog)
        self.dialog_message = None

    def draw_right_panel(self):
        # Draw the base right panel from the parent class
        super().draw_right_panel()

        # Draw "Choose" button
        pygame.draw.rect(self.screen, self.action_button_color, self.choose_button_rect)
        choose_txt = self.font.render("Choose", True, (0, 0, 0))
        self.screen.blit(choose_txt, choose_txt.get_rect(center=self.choose_button_rect.center))

        # Draw "Abandon" button
        pygame.draw.rect(self.screen, self.action_button_color, self.abandon_button_rect)
        abandon_txt = self.font.render("Abandon", True, (0, 0, 0))
        self.screen.blit(abandon_txt, abandon_txt.get_rect(center=self.abandon_button_rect.center))

        # Draw dialog if needed
        if self.dialog_message:
            self.draw_dialog(self.dialog_message)

    def draw_dialog(self, message):
        # Dialog box size and position (centered)
        w, h = 500, 120
        x = (self.screen.get_width() - w) // 2
        y = (self.screen.get_height() - h) // 2
        rect = pygame.Rect(x, y, w, h)

        # Background
        pygame.draw.rect(self.screen, (255, 255, 255), rect)
        pygame.draw.rect(self.screen, (0, 0, 0), rect, 4)

        # --- Word wrap ---
        max_width = w - 40  # margins inside the box
        words = message.split(" ")
        lines = []
        current = ""

        for word in words:
            test = current + word + " "
            if self.font.size(test)[0] <= max_width:
                current = test
            else:
                lines.append(current)
                current = word + " "
        lines.append(current)

        # Draw text centered vertically
        total_height = len(lines) * self.font.get_height()
        start_y = rect.centery - total_height // 2

        for i, line in enumerate(lines):
            text = self.font.render(line, True, (0, 0, 0))
            text_rect = text.get_rect(center=(rect.centerx, start_y + i * self.font.get_height()))
            self.screen.blit(text, text_rect)

    def handle_event(self, event):
        # If a dialog is open, any click closes it
        if self.dialog_message and event.type == pygame.MOUSEBUTTONDOWN:
            self.dialog_message = None
            return

        # Let the parent class handle scrolling, selection, exit button
        super().handle_event(event)

        # Handle action buttons
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos

            pokemons = self.get_pokedex().get_pokemons()
            if not pokemons:
                return

            current_pokemon = pokemons[self.selected_index]

            # Choose as combat Pokémon
            if self.choose_button_rect.collidepoint(mx, my):
                self.get_pokedex().choose_as_combat_pokemon(current_pokemon)
                self.dialog_message = f"{current_pokemon.get_name()} has been chosen as your combat Pokémon!"
                return

            # Abandon Pokémon
            if self.abandon_button_rect.collidepoint(mx, my):

                # Prevent abandoning the last Pokémon
                if len(self.get_pokedex().get_pokemons()) <= 1:
                    self.dialog_message = "You cannot abandon your only Pokémon!"
                    return

                # Prevent abandoning the combat Pokémon
                if self.get_pokedex().combat_pokemon is current_pokemon:
                    self.dialog_message = "You cannot abandon your combat Pokémon! Swap it first."
                    return

                # Remove Pokémon normally
                self.get_pokedex().abandon_pokemon(current_pokemon)

                # Adjust selection index if needed
                if self.selected_index >= len(self.get_pokedex().get_pokemons()):
                    self.selected_index = max(0, len(self.get_pokedex().get_pokemons()) - 1)

                self.load_current_pokemon_display()
                return