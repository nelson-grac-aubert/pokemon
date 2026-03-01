import pygame
from scripts.classes.PokedexDisplay_class import PokedexDisplay
from scripts.classes.PokemonDisplay_class import PokemonDisplay

class RegisteredPokedexDisplay(PokedexDisplay):

    def __init__(self, pokedex, screen):
        super().__init__(pokedex, screen)

        # PC button
        bx = self.back_button_rect.x
        by = self.back_button_rect.y - 60
        bw = self.back_button_rect.width
        bh = self.back_button_rect.height
        self.pc_button_rect = pygame.Rect(bx, by, bw, bh)

        # Switch flag
        self.request_pc_switch = False

        # Bigger sprite
        self.sprite_scale = 4.0

        if self.get_pokedex().get_pokemons():
            self.load_current_pokemon_display()

    def load_current_pokemon_display(self):
        pokemon = self.get_pokedex().get_pokemons()[self.selected_index]
        self.current_display = PokemonDisplay(pokemon, scale=self.sprite_scale, is_front=True)
        self.current_display.set_position(self.left_width + 350, 220)

    def draw_right_panel(self):
        super().draw_right_panel()

        # PC button
        pygame.draw.rect(self.screen, (200, 50, 50), self.pc_button_rect)
        pc_txt = self.font.render("PC", True, (255, 255, 255))
        self.screen.blit(pc_txt, pc_txt.get_rect(center=self.pc_button_rect.center))

        pokemons = self.get_pokedex().get_pokemons()
        if not pokemons:
            return

        pokemon = pokemons[self.selected_index]

        # Name + ID
        name_text = self.font.render(f"{pokemon.get_name()}  #{pokemon.get_id()}", True, (0, 0, 0))
        self.screen.blit(name_text, (self.left_width + 20, 20))

        # Types
        type_y = 70
        for t in pokemon.get_types():
            self.draw_type_rectangle(str(t.get_name()), self.left_width + 20, type_y)
            type_y += 40

        # Encounter count
        count = self.get_pokedex().get_encounter_count(pokemon)
        enc_text = self.font.render(f"Encounters number: {count}", True, (0, 0, 0))
        self.screen.blit(enc_text, (self.left_width + 20, 160))

        # Sprite
        if self.current_display:
            self.current_display.update()
            self.current_display.draw(self.screen)

    def handle_event(self, event):
        super().handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = event.pos

            # Switch to PC
            if self.pc_button_rect.collidepoint(mx, my):
                self.request_pc_switch = True
                return