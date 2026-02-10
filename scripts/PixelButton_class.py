import pygame
from assets_management import load_font
from colors import * 

pygame.init()
FONT = load_font("../assets/font/Pokemon_GB.ttf", 22)

class PixelButton:
    def __init__(self, text : str, x : int, y : int, w : int, h, color : tuple, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.base_rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = tuple(min(255, c + 25) for c in color)
        self.callback = callback

        self.scale = 1.0           # For hover effect
        self.pressed = False

    def draw(self, surface : pygame.Surface, mouse_pos : tuple):
        """
        Draw a pixel font button 
        
        :param self: Description
        :param surface: Pygame Surface of the button
        :type surface: pygame.Surface
        :param mouse_pos: x,y tuple position of the mouse accessed by pygame.mouse.get_pos()
        :type mouse_pos: tuple
        """

        hovered = self.rect.collidepoint(mouse_pos)

        # Handle hover and press for resizing and recoloring
        if hovered and not self.pressed:
            self.scale = min(1.05, self.scale + 0.05)
        elif not hovered and not self.pressed:
            self.scale = max(1.0, self.scale - 0.05)

        if self.pressed:
            self.scale = max(0.95, self.scale - 0.1)

        # 
        new_w = int(self.base_rect.width * self.scale)
        new_h = int(self.base_rect.height * self.scale)
        self.rect = pygame.Rect(
            self.base_rect.centerx - new_w // 2,
            self.base_rect.centery - new_h // 2,
            new_w, new_h)

        color = self.hover_color if hovered else self.color

        # Button background and black border
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 4)

        # Text 
        text_surf = FONT.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def update(self, mouse_pos : tuple, mouse_click : bool):
        """
        Handle PixelButton key press
        
        :param mouse_pos: x,y position of the mouse accessed with pygame.mouse.get_pos()
        :type mouse_pos: tuple
        :param mouse_click: True if mouse is clicked, False otherwise
        :type mouse_click: bool
        """
        if mouse_click and self.rect.collidepoint(mouse_pos):
            self.pressed = True
            self.callback()
        else:
            self.pressed = False