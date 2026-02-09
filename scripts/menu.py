import pygame
import sys
from assets_management import load_font
from all_pokemons import pikachu
from PokemonDisplay_class import PokemonDisplay

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

TITLE_FONT = load_font("../assets/font/Pokemon_GB.ttf", 48)
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

        # Animation hover
        if hovered and not self.pressed:
            self.scale = min(1.05, self.scale + 0.05)
        elif not hovered and not self.pressed:
            self.scale = max(1.0, self.scale - 0.05)

        # Animation press
        if self.pressed:
            self.scale = max(0.95, self.scale - 0.1)

        # Appliquer le scale
        new_w = int(self.base_rect.width * self.scale)
        new_h = int(self.base_rect.height * self.scale)
        self.rect = pygame.Rect(
            self.base_rect.centerx - new_w // 2,
            self.base_rect.centery - new_h // 2,
            new_w,
            new_h
        )

        # Couleur
        color = self.hover_color if hovered else self.color

        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BLACK, self.rect, 4)

        # Texte centré
        text_surf = FONT.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def update(self, mouse_pos, mouse_click):
        if mouse_click and self.rect.collidepoint(mouse_pos):
            self.pressed = True
            self.callback()
        else:
            self.pressed = False


def new_game():
    print("Nouvelle partie !")

def resume_game():
    print("Reprendre la partie !")

def quit_game():
    pygame.quit()
    sys.exit()

buttons = [
    PixelButton("NOUVELLE PARTIE", WIDTH//2 - 175, 300, 350, 60, RED, new_game),
    PixelButton("REPRENDRE",       WIDTH//2 - 175, 380, 350, 60, BLUE, resume_game),
    PixelButton("QUITTER",         WIDTH//2 - 175, 460, 350, 60, GREEN, quit_game),
]


def main_menu():
    while True:
        SCREEN.fill(BEIGE)

        title = TITLE_FONT.render("POKEMON", True, BLACK)
        title_rect = title.get_rect(center=(WIDTH//2, 100))
        SCREEN.blit(title, title_rect)
       
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
