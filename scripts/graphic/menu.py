import pygame
import sys
from scripts.logic.assets_management import load_font, load_image, load_gif
from scripts.logic.json_management import *
from scripts.classes.Pokedex_class import Pokedex, kanto_pokedex
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

# Animated pikachu on main menu 
pikachu_display = PokemonDisplay(kanto_pokedex.get_pokemons()[24], scale=2.3, is_front=True)
pikachu_display.set_position(width // 2, 235)

# Pokedex button
button_img = load_image("assets/images/pokedex.png").convert_alpha()
button_img = pygame.transform.scale(button_img, (90, 120))  # Resize pokedex image
button_img_rect = button_img.get_rect()
button_img_rect.topright = (width - 10, 10)  # Top-right
button_hover_scale = 1.0
button_target_scale = 1.0
button_click_cooldown = 0

# Buttons functions 
def new_game():
    player_pokedex = run_game_intro(screen, clock, kanto_pokedex)
    return player_pokedex

def resume_game():
    print("Reprendre la partie !")

def quit_game():
    pygame.quit()
    sys.exit()

def options() : 
    pass

# UI Buttons
buttons = [PixelButton("NEW GAME", width//2 - 175, 300, 350, 60, DARKBLUE, new_game),
        PixelButton("RESUME GAME", width//2 - 175, 370, 350, 60, DARKGREEN, resume_game),
        PixelButton("OPTIONS", width//2 - 175, 440, 350, 60, DARKTEAL, options),
        PixelButton("QUIT", width//2 - 175, 510, 350, 60, SAGEGREEN, quit_game)]

def draw_pokedex_button(surface, image, rect, scale):
    w, h = image.get_size()
    scaled_img = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    new_rect = scaled_img.get_rect(center=rect.center)
    surface.blit(scaled_img, new_rect)

def main_menu():
    run_intro(screen, clock, kanto_pokedex)

    # Animated menu background
    background_frames = load_gif("assets/images/bmenu2.gif", size=(width, height))
    current_frame = 0
    frame_delay = 5  
    frame_counter = 0

    while True:
        # Animate background
        frame_counter += 1
        if frame_counter >= frame_delay:
            current_frame = (current_frame + 1) % len(background_frames)
            frame_counter = 0

        screen.blit(background_frames[current_frame], (0, 0))

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

        # Hover pokedex button
        if button_img_rect.collidepoint(mouse_pos):
            button_target_scale = 1.15  # zoom 
        else:
            button_target_scale = 1.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_click = True

        # Click pokedex button
                if button_img_rect.collidepoint(mouse_pos):
                    button_click_cooldown = 5
                    run_pokedex(kanto_pokedex)

        for btn in buttons:
            btn.update(mouse_pos, mouse_click)
            btn.draw(screen, mouse_pos)
        
        # Resize pokedex button on hover
        button_hover_scale += (button_target_scale - button_hover_scale) * 0.15 
        if button_click_cooldown > 0 :
           button_hover_scale = 0.9
           button_click_cooldown -= 1

        draw_pokedex_button(screen, button_img, button_img_rect, button_hover_scale)

        pygame.display.flip()
        clock.tick(fps)

main_menu()