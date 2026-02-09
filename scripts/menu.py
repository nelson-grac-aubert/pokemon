import pygame
import sys
from assets_management import load_font
from all_pokemons import pikachu
from PokemonDisplay_class import PokemonDisplay
from PixelButton_class import PixelButton
from colors import * 

pygame.init()
FPS = 60
CLOCK = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
TITLE_FONT = load_font("../assets/font/Pokemon_GB.ttf", 48)

pygame.display.set_caption("Menu Pokémon Pixel")

pikachu_display = PokemonDisplay(pikachu, scale=2.0, is_front=True)
pikachu_display.set_position(WIDTH // 2, 200)

def new_game():
    print("Nouvelle partie !")

def resume_game():
    print("Reprendre la partie !")

def quit_game():
    pygame.quit()
    sys.exit()

buttons = [PixelButton("NOUVELLE PARTIE", WIDTH//2 - 175, 300, 350, 60, RED, new_game),
        PixelButton("REPRENDRE", WIDTH//2 - 175, 380, 350, 60, BLUE, resume_game),
        PixelButton("QUITTER", WIDTH//2 - 175, 460, 350, 60, GREEN, quit_game)]

def main_menu():
    while True:
        SCREEN.fill(BEIGE)

        title = TITLE_FONT.render("POKEMON", True, BLACK)
        title_rect = title.get_rect(center=(WIDTH//2, 100))
        SCREEN.blit(title, title_rect)

        pikachu_display.update()
        pikachu_display.draw(SCREEN)

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