import pygame
from scripts.logic.assets_management import load_font
from scripts.classes.Pokedex_class import Pokedex
from scripts.classes.PokemonDisplay_class import PokemonDisplay
from scripts.graphic.colors import TYPE_COLORS

class PokedexDisplay:
    def __init__(self, pokedex: Pokedex, screen: pygame.Surface):
        self.__pokedex = pokedex
        self.screen = screen

        # Selection
        self.selected_index = 0

        # Exit flag
        self.request_exit = False

        # Layout
        self.left_width = 260
        self.right_width = screen.get_width() - self.left_width

        # Back button
        self.back_button_rect = pygame.Rect(self.left_width + 20, self.screen.get_height() - 60, 160, 40)

        # Scroll
        self.scroll_offset = 0
        self.scroll_speed = 30
        self.line_height = 48

        # Fonts
        self.font = load_font("assets/font/Pokemon_GB.ttf", 18)
        self.small_font = load_font("assets/font/Pokemon_GB.ttf", 14)

        # Animated Pokémon
        self.current_display = None
        if self.__pokedex.get_pokemons():
            self.load_current_pokemon_display()

    def get_pokedex(self):
        return self.__pokedex

    def draw(self):
        self.draw_left_panel()
        self.draw_right_panel()

    def load_current_pokemon_display(self):
        pokemon = self.__pokedex.get_pokemons()[self.selected_index]
        self.current_display = PokemonDisplay(pokemon, scale=3.0, is_front=True)
        self.current_display.set_position(self.left_width + 350, 200)

    def draw_left_panel(self):
        """ Draw left pannel, a scrollable Pokemon list """
        pygame.draw.rect(
            self.screen,
            (220, 0, 0),
            (0, 0, self.left_width, self.screen.get_height())
        )

        pokemons = self.__pokedex.get_pokemons()

        for i, pokemon in enumerate(pokemons):
            y = i * self.line_height - self.scroll_offset

            # Skip lines outside screen
            if y < -self.line_height or y > self.screen.get_height():
                continue

            rect = pygame.Rect(0, y, self.left_width, self.line_height)

            if i == self.selected_index:
                pygame.draw.rect(self.screen, (255, 180, 180), rect)
            else:
                pygame.draw.rect(self.screen, (255, 230, 230), rect)

            text = self.font.render(
                f"{pokemon.get_id()} {pokemon.get_name()}",
                True,
                (0, 0, 0)
            )
            self.screen.blit(text, (10, y + 10))

    def draw_type_rectangle(self, type_name : str, x : int, y : int):
        """
        Draw a rectangle with the Pokemon type, with a matching color 
        
        :param type_name: Name of that Type
        :type type_name: str
        :param x: Horizontal position of the box
        :type x: int
        :param y: Vertical position of the box 
        :type y: int
        """
        type_box_width = 120
        type_box_height = 32

        # Pick color based on type
        color = TYPE_COLORS.get(type_name.lower(), (210, 210, 210))

        type_rect = pygame.Rect(x, y, type_box_width, type_box_height)
        pygame.draw.rect(self.screen, color, type_rect)

        type_label = self.small_font.render(type_name, True, (0, 0, 0))
        text_rect = type_label.get_rect(center=type_rect.center)
        self.screen.blit(type_label, text_rect)


    def draw_right_panel(self):
        """ Draw right pannel, showing pokemon name, stats and animated sprite """
        pygame.draw.rect(
            self.screen,
            (245, 245, 245),
            (self.left_width, 0, self.right_width, self.screen.get_height())
        )

        # Return button
        pygame.draw.rect(self.screen, (200, 50, 50), self.back_button_rect)
        txt = self.font.render("Main menu", True, (255, 255, 255))
        self.screen.blit(txt, (self.back_button_rect.x + 10, self.back_button_rect.y + 8))

        pokemons = self.__pokedex.get_pokemons()
        if not pokemons:
            return

        pokemon = pokemons[self.selected_index]

        # Name + ID
        name_text = self.font.render(
            f"{pokemon.get_name()}  #{pokemon.get_id()}",
            True,
            (0, 0, 0)
        )
        self.screen.blit(name_text, (self.left_width + 20, 20))

        # Rectangles with types
        type_y = 70
        for t in pokemon.get_types():
            self.draw_type_rectangle(str(t.get_name()), self.left_width + 20, type_y)
            type_y += 40


        # Stats
        stats_y = 160
        stats = [
            ("HP", pokemon.get_hp()),
            ("ATK", pokemon.get_attack()),
            ("DEF", pokemon.get_defense()),
            ("SPD", pokemon.get_speed()),
            ("PREC", pokemon.get_precision())
        ]

        for label, value in stats:
            txt = self.font.render(f"{label}: {value}", True, (0, 0, 0))
            self.screen.blit(txt, (self.left_width + 20, stats_y))
            stats_y += 40

        if self.current_display:
            self.current_display.update()
            self.current_display.draw(self.screen)


    # Inputs
    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Scroll list of pokemon
            if event.button == 4:
                self.scroll_offset = max(self.scroll_offset - self.scroll_speed, 0)
                return

            elif event.button == 5:
                self.scroll_offset += self.scroll_speed
                return

            # Left click
            if event.button == 1:
                mx, my = event.pos

                # Main menu button
                if self.back_button_rect.collidepoint(mx, my):
                    self.request_exit = True
                    return

                # Select a pokemon
                if mx < self.left_width:
                    index = (my + self.scroll_offset) // self.line_height
                    if 0 <= index < len(self.__pokedex.get_pokemons()):
                        self.selected_index = index
                        self.load_current_pokemon_display()

