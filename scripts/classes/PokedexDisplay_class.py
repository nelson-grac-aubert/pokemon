import pygame
from scripts.classes.Pokedex_class import Pokedex

class PokedexDisplay:
    def __init__(self, pokedex: Pokedex, screen: pygame.Surface):
        self.__pokedex = pokedex
        self.screen = screen

        # Layout
        self.left_width = 260
        self.right_width = screen.get_width() - self.left_width

        # Scroll
        self.scroll_offset = 0
        self.scroll_speed = 30
        self.line_height = 48

        # Selection
        self.selected_index = 0

        # Fonts
        self.font = pygame.font.Font(None, 28)
        self.small_font = pygame.font.Font(None, 22)

    def get_pokedex(self):
        return self.__pokedex

    def draw(self):
        self.draw_left_panel()
        self.draw_right_panel()

    # -------------------------------------------------------------------------
    # Left panel : pokemon list
    # -------------------------------------------------------------------------
    def draw_left_panel(self):
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
                f"#{pokemon.get_id()}  {pokemon.get_name()}",
                True,
                (0, 0, 0)
            )
            self.screen.blit(text, (10, y + 10))

    # -------------------------------------------------------------------------
    # Right panel : pokemon infos
    # -------------------------------------------------------------------------
    def draw_right_panel(self):
        pygame.draw.rect(
            self.screen,
            (245, 245, 245),
            (self.left_width, 0, self.right_width, self.screen.get_height())
        )

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

        # Types (rect gris + nom du type)
        type_y = 70
        for t in pokemon.get_types():
            type_rect = pygame.Rect(self.left_width + 20, type_y, 90, 28)
            pygame.draw.rect(self.screen, (210, 210, 210), type_rect)

            # get_name()
            type_label = self.small_font.render(str(t.get_name()), True, (0, 0, 0))
            self.screen.blit(type_label, (self.left_width + 25, type_y + 4))

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

        # Animated frames (si déjà chargées quelque part)
        if getattr(pokemon, "front_frames", None):
            if pokemon.front_frames:
                frame = pokemon.front_frames[pokemon.frame_index]
                self.screen.blit(frame, (self.left_width + 250, 80))

    # -------------------------------------------------------------------------
    # Inputs
    # -------------------------------------------------------------------------
    def handle_event(self, event):
        # Scroll
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # molette haut
                self.scroll_offset = max(self.scroll_offset - self.scroll_speed, 0)
            elif event.button == 5:  # molette bas
                self.scroll_offset += self.scroll_speed

            # Click a pokemon
            if event.button == 1:
                mx, my = event.pos

                if mx < self.left_width:
                    index = (my + self.scroll_offset) // self.line_height

                    if 0 <= index < len(self.__pokedex.get_pokemons()):
                        self.selected_index = index
