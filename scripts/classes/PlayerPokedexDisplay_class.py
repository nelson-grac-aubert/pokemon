import pygame
from PokedexDisplay_class import PokedexDisplay

class PlayerPokedexDisplay(PokedexDisplay) : 
    def __init__(self, screen) : 
        super().__init__(self, screen)

    def draw_chose_button(self) : 
        pass

    def draw_abandon_button(self) : 
        abandon_button_rect = pygame.Rect(self.screen.get_width() - 400, self.screen.get_height() - 60, 180, 40)
        abandon_button_text = self.font.render("Abandon", True, (255, 255, 255))
        abandon_text_rect = abandon_button_text.get_rect(center=self.abandon_button_rect.center)

        pygame.draw.rect(self.screen, (200, 50, 50), abandon_button_rect)
        self.screen.blit(abandon_button_text, abandon_text_rect)

    def draw_right_panel(self):
        super().draw_right_panel()
        self.draw_abandon_button()
        self.draw_chose_button()

