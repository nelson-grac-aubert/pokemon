import pygame
import sys
from assets_management import load_font

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu Pokémon Pixel")

FPS = 60
CLOCK = pygame.time.Clock()

RED = (200, 70, 70)
BLUE = (90, 120, 170)
GREEN = (100, 160, 100)
BEIGE = (230, 220, 180)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FONT = load_font("../assets/font/Pokemon_GB.ttf", 32)

class PixelButton:
    def __init__(self, text, x, y, w, h, color, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.hover_color = tuple(min(255, c + 30) for c in color)
        self.callback = callback

    def draw(self, surface, mouse_pos):
        
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(surface, self.hover_color, self.rect)
            pygame.draw.rect(surface, WHITE, self.rect, 4)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
            pygame.draw.rect(surface, BLACK, self.rect, 4)

        text_surf = FONT.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def update(self, mouse_pos, mouse_click):
        if mouse_click and self.rect.collidepoint(mouse_pos):
            self.callback()

def new_game():
    print("Nouvelle partie !")

def resume_game():
    print("Reprendre la partie !")

def quit_game():
    pygame.quit()
    sys.exit()


buttons = [
    PixelButton("NOUVELLE PARTIE", WIDTH//2 - 150, 250, 300, 70, RED, new_game),
    PixelButton("REPRENDRE",       WIDTH//2 - 150, 340, 300, 70, BLUE, resume_game),
    PixelButton("QUITTER",         WIDTH//2 - 150, 430, 300, 70, GREEN, quit_game),
]

def main_menu():
    while True:
        SCREEN.fill(BEIGE)

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_click = True

        for btn in buttons:
            btn.update(mouse_pos, mouse_click)
            btn.draw(SCREEN, mouse_pos)

        pygame.display.flip()
        CLOCK.tick(FPS)


main_menu()
