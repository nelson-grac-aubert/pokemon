import pygame
import sys
from scripts.logic.assets_management import (
    load_font, load_image, load_gif,
    button_music_click, draw_music_button, 
    button_sound_click
)
from scripts.logic.json_management import *
from scripts.classes.Pokedex_class import kanto_pokedex
from scripts.classes.PokemonDisplay_class import PokemonDisplay
from scripts.classes.PixelButton_class import PixelButton
from scripts.classes.SoundControl_class import sound_control
from scripts.graphic.colors import * 
from scripts.graphic.pokedex_menu import run_pokedex
from scripts.graphic.menu_intro import run_intro
from scripts.graphic.game_intro import run_game_intro

# --- INIT ---
pygame.init()
fps = 60
clock = pygame.time.Clock()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("PokePixel")
title_font = load_font("assets/font/Pokemon_GB.ttf", 48)

# --- GLOBAL MENU STATE ---
MENU_STATE = "main"  # "main" ou "options"

# --- PIKACHU ---
pikachu_display = PokemonDisplay(kanto_pokedex.get_pokemons()[24], scale=2.3, is_front=True)
pikachu_display.set_position(width // 2, 235)

# --- POKEDEX BUTTON ---
button_img = load_image("assets/images/pokedex.png").convert_alpha()
button_img = pygame.transform.scale(button_img, (90, 120))
button_img_rect = button_img.get_rect()
button_img_rect.topright = (width - 10, 10)
button_hover_scale = 1.0
button_target_scale = 1.0
button_click_cooldown = 0

# --- BUTTON CALLBACKS ---
def new_game():
    player_pokedex = run_game_intro(screen, clock, kanto_pokedex)
    return player_pokedex

def resume_game():
    print("Reprendre la partie !")

def quit_game():
    pygame.quit()
    sys.exit()

def options():
    global MENU_STATE
    MENU_STATE = "options"

def back_to_menu():
    global MENU_STATE
    MENU_STATE = "main"

# --- UI BUTTONS ---
buttons = [
    PixelButton("NEW GAME", width//2 - 175, 300, 350, 60, DARKBLUE, new_game),
    PixelButton("RESUME GAME", width//2 - 175, 370, 350, 60, DARKGREEN, resume_game),
    PixelButton("OPTIONS", width//2 - 175, 440, 350, 60, DARKTEAL, options),
    PixelButton("QUIT", width//2 - 175, 510, 350, 60, SAGEGREEN, quit_game)
]
back_button = PixelButton("BACK", width//2 - 175, 500, 350, 60, DARKBLUE, back_to_menu)

def draw_pokedex_button(surface, image, rect, scale):
    w, h = image.get_size()
    scaled_img = pygame.transform.scale(image, (int(w * scale), int(h * scale)))
    new_rect = scaled_img.get_rect(center=rect.center)
    surface.blit(scaled_img, new_rect)

def main_menu():
    global button_hover_scale, button_target_scale, button_click_cooldown, MENU_STATE

    run_intro(screen, clock, kanto_pokedex)

    # --- MUSIC ---
    sound_control.play_music("assets/music/opening.mp3")
    music_img = load_image("assets/images/music.png").convert_alpha()
    music_muted_img = load_image("assets/images/music_off.png").convert_alpha()
    music_muted = False

    sound_img = load_image("assets/images/sound.png").convert_alpha()
    sound_muted_img = load_image("assets/images/sound_off.png").convert_alpha()
    sound_muted = False

    # Taille réduite (par exemple 64x64)
    icon_size = (90, 90)

    music_img = pygame.transform.scale(music_img, icon_size)
    music_muted_img = pygame.transform.scale(music_muted_img, icon_size)

    sound_img = pygame.transform.scale(sound_img, icon_size)
    sound_muted_img = pygame.transform.scale(sound_muted_img, icon_size)


    # --- BACKGROUND ---
    background_frames = load_gif("assets/images/bmenu2.gif", size=(width, height))
    current_frame = 0
    frame_delay = 5  
    frame_counter = 0

    # --- TITLE (chargé une seule fois) ---
    title = load_image("assets/images/logo.png")
    title = pygame.transform.scale(title, (500, 500))
    title_rect = title.get_rect(center=(width//2, 100))

    while True:

        # --- ANIMATION DU FOND (uniquement dans le menu principal) ---
        frame_counter += 1
        if frame_counter >= frame_delay:
            current_frame = (current_frame + 1) % len(background_frames)
            frame_counter = 0

        # --- AFFICHAGE SELON L'ÉTAT ---
        if MENU_STATE == "main":
            # Fond animé
            screen.blit(background_frames[current_frame], (0, 0))

            # Titre
            screen.blit(title, title_rect)

            # Pikachu
            pikachu_display.update()
            pikachu_display.draw(screen)

        elif MENU_STATE == "options":
            # Fond simple
            screen.blit(background_frames[current_frame], (0, 0))


        # --- EVENTS ---
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = False

        # Hover pokedex button (uniquement en main)
        if MENU_STATE == "main" and button_img_rect.collidepoint(mouse_pos):
            button_target_scale = 1.15
        else:
            button_target_scale = 1.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_click = True

                # Click pokedex button (uniquement en main)
                if MENU_STATE == "main" and button_img_rect.collidepoint(mouse_pos):
                    button_click_cooldown = 5
                    run_pokedex(kanto_pokedex)

            # Gestion du mute dans OPTIONS
            if MENU_STATE == "options":
                center_rect = music_img.get_rect(center=(width//2 + 80, height//10))
                music_muted = button_music_click(event, center_rect, music_muted)

                sound_rect = sound_img.get_rect(center=(width//2 - 80, height//10)) 
                sound_muted = button_sound_click(event, sound_rect, sound_muted) 
                sound_control.sound_muted = sound_muted 

        # --- DESSIN DES BOUTONS SELON L'ÉTAT ---
        if MENU_STATE == "main":
            for btn in buttons:
                btn.update(mouse_pos, mouse_click)
                btn.draw(screen, mouse_pos)

            # Bouton Pokédex
            draw_pokedex_button(screen, button_img, button_img_rect, button_hover_scale)

        elif MENU_STATE == "options":

            sound_rect  = sound_img.get_rect(center=(width//2 - 80, height//10))
            draw_music_button(screen, sound_muted, sound_img, sound_muted_img, sound_rect)

            center_rect = music_img.get_rect(center=(width//2 + 80, height//10))
            draw_music_button(screen, music_muted, music_img, music_muted_img, center_rect)

            back_button.update(mouse_pos, mouse_click)
            back_button.draw(screen, mouse_pos)

        # --- ANIMATION DU POKEDEX ---
        if MENU_STATE == "main":
            button_hover_scale += (button_target_scale - button_hover_scale) * 0.15 
            if button_click_cooldown > 0:
                button_hover_scale = 0.9
                button_click_cooldown -= 1

        pygame.display.flip()
        clock.tick(fps)

main_menu()
