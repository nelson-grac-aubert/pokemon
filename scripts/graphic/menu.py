import pygame
import sys
from scripts.logic.assets_management import load_font, load_image
from scripts.logic.json_management import *
from scripts.classes.Pokedex_class import Pokedex
from scripts.classes.PokemonDisplay_class import PokemonDisplay
from scripts.classes.PixelButton_class import PixelButton
from scripts.graphic.colors import * 
from scripts.graphic.pokedex_menu import run_pokedex
from scripts.classes.SoundControl_class import sound_control
from scripts.graphic.menu_intro import run_intro
from scripts.graphic.game_intro import run_game_intro

# Initialize pygame screen variables
pygame.init()
fps = 60
clock = pygame.time.Clock()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PokePixel")
title_font = load_font("assets/font/Pokemon_GB.ttf", 48)

# Sounds 
sound_control.play_music("assets/music/opening.mp3")

# Load Pokedex for gif display on menu 
kanto_pokedex = Pokedex()
kanto_pokedex.set_pokemons(load_pokemons_from_json("assets/data/all_pokemons.json", 
                        load_types_from_json("assets/data/all_types.json")))

# Animated pikachu on main menu 
pikachu_display = PokemonDisplay(kanto_pokedex.get_pokemons()[24], scale=2.3, is_front=True)
pikachu_display.set_position(width // 2, 235)

button_img = load_image("assets/images/pokedex.png").convert_alpha()
button_img = pygame.transform.scale(button_img, (140, 120))  # adapte la taille 
button_img_rect = button_img.get_rect()
button_img_rect.topright = (width - 20, 20)  # position en haut à droite
button_hover_scale = 1.0
button_target_scale = 1.0
button_click_cooldown = 0

# Buttons functions 

def new_game():
    player_pokedex, starter = run_game_intro(screen, clock, kanto_pokedex)
    return player_pokedex

def resume_game():
    print("Reprendre la partie !")

def quit_game():
    pygame.quit()
    sys.exit()


buttons = [PixelButton("NEW GAME", width//2 - 175, 300, 350, 60, RED, new_game),
        PixelButton("RESUME GAME", width//2 - 175, 380, 350, 60, BLUE, resume_game),
        PixelButton("QUIT", width//2 - 175, 460, 350, 60, GREEN, quit_game)]

def draw_animated_button(surface, image, rect, scale):
    w, h = image.get_size()
    scaled_img = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    new_rect = scaled_img.get_rect(center=rect.center)
    surface.blit(scaled_img, new_rect)

def main_menu():
    run_intro(screen, clock, kanto_pokedex)

    while True:
        screen.fill(BEIGE)

        # Title
        title = load_image("assets/images/logo.png")
        size = (500, 500)
        title = pygame.transform.scale(title, size)

        title_rect = title.get_rect(center=(width//2, 100))
        screen.blit(title, title_rect)

        # Animate pikachu on screen 
        pikachu_display.update()
        pikachu_display.draw(screen)

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
                    run_pokedex(kanto_pokedex)

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