import pygame
import random
from scripts.logic.assets_management import load_image
from scripts.graphic.pokedex_menu import run_pokedex
from scripts.graphic.menu import sound_control
from scripts.classes.Combat_class import Combat

def overworld_game_loop(screen, clock, starter_pokemon, player_pokedex):

    sound_control.play_music("assets/music/road_1.mp3")

    width, height = screen.get_size()

    # Load and scale the background map
    background = load_image("assets/images/game_map.png")
    background = pygame.transform.scale(background, (width, height))

    # Load the player sprite
    player_sprite = load_image("assets/sprites/player_sprite_single.png")

    # Player position
    player_x = width // 2
    player_y = height // 2
    speed = 3

    # --- Pokédex button ---
    pokedex_button = load_image("assets/images/pokedex.png").convert_alpha()
    pokedex_button = pygame.transform.scale(pokedex_button, (90, 120))
    pokedex_rect = pokedex_button.get_rect()
    pokedex_rect.topright = (width - 20, 20)

    # --- Step counter system ---
    walking_time = 0  # accumulated time spent walking
    next_encounter_time = random.uniform(4, 5)  # random threshold in seconds

    running = True
    while running:

        dt = clock.get_time() / 1000  # seconds since last frame

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Click on Pokédex button
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pokedex_rect.collidepoint(event.pos):
                    run_pokedex(player_pokedex)

        # Move player
        keys = pygame.key.get_pressed()
        moving = False

        if keys[pygame.K_UP]:
            player_y -= speed
            moving = True
        if keys[pygame.K_DOWN]:
            player_y += speed
            moving = True
        if keys[pygame.K_LEFT]:
            player_x -= speed
            moving = True
        if keys[pygame.K_RIGHT]:
            player_x += speed
            moving = True

        # --- Step counter logic ---
        if moving:
            walking_time += dt
            if walking_time >= next_encounter_time:
                sound_control.play_music("assets/music/battle.mp3")
                walking_time = 0
                next_encounter_time = random.uniform(4, 5)

                combat = Combat(player_pokedex)
                combat.run(screen, clock)

        # UI
        screen.blit(background, (0, 0))

        # Draw player centered
        player_rect = player_sprite.get_rect(center=(player_x, player_y))
        screen.blit(player_sprite, player_rect)

        # Draw Pokédex button
        screen.blit(pokedex_button, pokedex_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
