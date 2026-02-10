import pygame
import sys
from scripts.logic.assets_management import load_font, load_image
from scripts.data.all_pokemons import bulbasaur
from scripts.classes.PokemonDisplay_class import PokemonDisplay
from scripts.classes.PixelButton_class import PixelButton
from scripts.graphic.colors import * 

pygame.init()
fps = 60
clock = pygame.time.Clock()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
title_font = load_font("assets/font/Pokemon_GB.ttf", 48)

pygame.display.set_caption("Menu Pokémon Pixel")

bulbasaur_display = PokemonDisplay(bulbasaur, scale=2.0, is_front=True)
bulbasaur_display.set_position(width // 2, 200)

button_img = load_image("assets/images/pokedex.png").convert_alpha()
button_img = pygame.transform.scale(button_img, (140, 120))  # adapte la taille 
button_img_rect = button_img.get_rect()
button_img_rect.topright = (width - 20, 20)  # position en haut à droite
button_hover_scale = 1.0
button_target_scale = 1.0
button_click_cooldown = 0


# Buttons functions 
def new_game():
    print("Nouvelle partie !")

def resume_game():
    print("Reprendre la partie !")

def quit_game():
    pygame.quit()
    sys.exit()


buttons = [PixelButton("NEW GAME", width//2 - 175, 300, 350, 60, RED, new_game),
        PixelButton("RESUME GAME", width//2 - 175, 380, 350, 60, BLUE, resume_game),
        PixelButton("QUIT", width//2 - 175, 460, 350, 60, GREEN, quit_game)]

def open_new_window():
    new_screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Nouvelle Fenêtre")

    back_img = load_image("assets/images/back_arrow.png").convert_alpha()
    back_img = pygame.transform.scale(back_img, (64, 64))
    back_rect = back_img.get_rect()
    back_rect.topleft = (20, 20)

    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_rect.collidepoint(mouse_pos):
                    running = False

        new_screen.fill((180, 200, 255))
        new_screen.blit(back_img, back_rect)

        pygame.display.flip()

    # Retour à la fenêtre principale
    pygame.display.set_mode((width, height))
    pygame.display.set_caption("Menu Pokémon Pixel")

def draw_animated_button(surface, image, rect, scale):
    w, h = image.get_size()
    scaled_img = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    new_rect = scaled_img.get_rect(center=rect.center)
    surface.blit(scaled_img, new_rect)



def main_menu():
    while True:
        screen.fill(BEIGE)

        # Title
        title = title_font.render("POKEMON", True, BLACK)
        title_rect = title.get_rect(center=(width//2, 100))
        screen.blit(title, title_rect)

        # Animate bulbasaur on screen 
        bulbasaur_display.update()
        bulbasaur_display.draw(screen)

        # Events
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False

        global button_hover_scale, button_target_scale, button_click_cooldown

# Hover
        if button_img_rect.collidepoint(mouse_pos):
            button_target_scale = 1.15  # zoom 
        else:
            button_target_scale = 1.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_click = True

        # Click
                if button_img_rect.collidepoint(mouse_pos):
                    button_click_cooldown = 5
                    open_new_window()

        for btn in buttons:
            btn.update(mouse_pos, mouse_click)
            btn.draw(screen, mouse_pos)
        
        button_hover_scale += (button_target_scale - button_hover_scale) * 0.15 
        if button_click_cooldown > 0 :
           button_hover_scale = 0.9
           button_click_cooldown -= 1

        draw_animated_button(screen, button_img, button_img_rect, button_hover_scale)

        btn.draw(screen, mouse_pos)

        pygame.display.flip()
        clock.tick(fps)

main_menu()