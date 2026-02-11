import pygame
from scripts.logic.assets_management import load_image
from scripts.graphic.pokedex_menu import run_pokedex

def overworld_game_loop(screen, clock, starter_pokemon, player_pokedex):
    width, height = screen.get_size()

    # Load and scale the background map
    background = load_image("assets/images/game_map.png")
    background = pygame.transform.scale(background, (width, height))

    # Load the player sprite
    player_sprite = load_image("assets/sprites/player_sprite_single.png")

    # Player position
    player_x = width // 2
    player_y = height // 2
    speed = 4

    # --- Pokédex button ---
    pokedex_button = load_image("assets/images/pokedex.png").convert_alpha()
    pokedex_button = pygame.transform.scale(pokedex_button, (120, 100))
    pokedex_rect = pokedex_button.get_rect()
    pokedex_rect.topright = (width - 20, 20)

    running = True
    while running:

        # --- EVENT HANDLING ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Click on Pokédex button
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pokedex_rect.collidepoint(event.pos):
                    run_pokedex(player_pokedex)  # open current pokedex

        # --- KEYBOARD INPUT ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_y -= speed
        if keys[pygame.K_DOWN]:
            player_y += speed
        if keys[pygame.K_LEFT]:
            player_x -= speed
        if keys[pygame.K_RIGHT]:
            player_x += speed

        # --- DRAWING ---
        screen.blit(background, (0, 0))

        # Draw player centered
        player_rect = player_sprite.get_rect(center=(player_x, player_y))
        screen.blit(player_sprite, player_rect)

        # Draw Pokédex button
        screen.blit(pokedex_button, pokedex_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()