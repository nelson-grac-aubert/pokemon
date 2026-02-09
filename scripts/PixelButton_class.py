import pygame
from assets_management import load_font
from colors import * 

pygame.init()
FONT = load_font("../assets/font/Pokemon_GB.ttf", 22)

class PixelButton:
    def __init__(self, text, x, y, w, h, color, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.base_rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = tuple(min(255, c + 25) for c in color)
        self.callback = callback

        self.scale = 1.0
        self.pressed = False

    def draw(self, surface, mouse_pos):
        hovered = self.rect.collidepoint(mouse_pos)

        if hovered and not self.pressed:
            self.scale = min(1.05, self.scale + 0.05)
        elif not hovered and not self.pressed:
            self.scale = max(1.0, self.scale - 0.05)

        if self.pressed:
            self.scale = max(0.95, self.scale - 0.1)

        new_w = int(self.base_rect.width * self.scale)
        new_h = int(self.base_rect.height * self.scale)
        self.rect = pygame.Rect(
            self.base_rect.centerx - new_w // 2,
            self.base_rect.centery - new_h // 2,
            new_w,
            new_h
        )

        color = self.hover_color if hovered else self.color

        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 4)

        text_surf = FONT.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def update(self, mouse_pos, mouse_click):
        if mouse_click and self.rect.collidepoint(mouse_pos):
            self.pressed = True
            self.callback()
        else:
            self.pressed = False