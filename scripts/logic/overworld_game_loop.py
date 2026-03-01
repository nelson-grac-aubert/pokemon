import pygame
import random
import copy
from scripts.logic.assets_management import load_image, load_font
from scripts.graphic.pokedex_menu import run_pokedex
from scripts.graphic.menu import sound_control
from scripts.classes.Combat import Combat
from scripts.graphic.EvolutionScreen import EvolutionScreen
from scripts.classes.DialogBox import DialogBox

def open_evolution_screen(screen, old_pokemon, new_pokemon):
    evolution_screen = EvolutionScreen(screen, old_pokemon, new_pokemon)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        evolution_screen.update()
        evolution_screen.draw()
        pygame.display.flip()

        clock.tick(60)

        if evolution_screen.is_finished():
            running = False

def handle_evolution(screen, background, player_sprite, pokedex_button, pokedex_rect,
                     dialog, pokemon, player_x, player_y, player_pokedex, registered_pokedex):

    old_pokemon = copy.deepcopy(pokemon)
    old_name = old_pokemon.get_name()

    dialog.show(f"Something is happening to {old_name}!")

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            dialog.handle_event(event)

        screen.blit(background, (0, 0))
        player_rect = player_sprite.get_rect(center=(player_x, player_y))
        screen.blit(player_sprite, player_rect)
        screen.blit(pokedex_button, pokedex_rect)

        dialog.draw()
        pygame.display.flip()

        if not dialog.is_open():
            waiting = False

    new_pokemon = pokemon.evolve()
    new_pokemon.set_level(pokemon.get_level())
    new_pokemon.set_xp(pokemon.get_xp())

    registered_pokedex.register_encounter(new_pokemon)
    player_pokedex.replace_combat_pokemon(new_pokemon)

    sound_control.play_music("assets/music/road_3.mp3")
    open_evolution_screen(screen, old_pokemon, new_pokemon)

    dialog.show(f"{old_name} has evolved into {new_pokemon.get_name()}!")

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            dialog.handle_event(event)

        screen.blit(background, (0, 0))
        player_rect = player_sprite.get_rect(center=(player_x, player_y))
        screen.blit(player_sprite, player_rect)
        screen.blit(pokedex_button, pokedex_rect)

        dialog.draw()
        pygame.display.flip()

        if not dialog.is_open():
            waiting = False

    sound_control.play_music("assets/music/road_1.mp3")

def overworld_game_loop(screen, clock, player_pokedex, registered_pokedex):

    sound_control.play_music("assets/music/road_1.mp3")
    font = load_font("assets/font/Pokemon_GB.ttf", 22)
    dialog = DialogBox(screen, font)

    width, height = screen.get_size()

    background = load_image("assets/images/game_map.png")
    background = pygame.transform.scale(background, (width, height))

    player_sprite = load_image("assets/sprites/player_sprite_single.png")

    player_x = width // 2
    player_y = height // 2
    speed = 3

    pokedex_button = load_image("assets/images/pokedex.png").convert_alpha()
    pokedex_button = pygame.transform.scale(pokedex_button, (90, 120))
    pokedex_rect = pokedex_button.get_rect()
    pokedex_rect.topright = (width - 20, 20)

    walking_time = 0
    next_encounter_time = random.uniform(4, 5)

    running = True
    while running:

        dt = clock.get_time() / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pokedex_rect.collidepoint(event.pos):
                    run_pokedex(player_pokedex, registered_pokedex)

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

        if moving:
            walking_time += dt
            if walking_time >= next_encounter_time:
                sound_control.play_music("assets/music/battle.mp3")
                walking_time = 0
                next_encounter_time = random.uniform(4, 5)

                combat = Combat(player_pokedex)

                # Register encountered pokémon into pokédex
                registered_pokedex.register_encounter(combat.get_adversary())

                winner = combat.run(screen, clock)

                pokemon = player_pokedex.combat_pokemon

                if pokemon.has_evolved():
                    handle_evolution(screen, background, player_sprite,
                    pokedex_button, pokedex_rect, dialog, pokemon,
                    player_x, player_y, player_pokedex, registered_pokedex)
                
                sound_control.play_music("assets/music/road_1.mp3")

        screen.blit(background, (0, 0))

        player_rect = player_sprite.get_rect(center=(player_x, player_y))
        screen.blit(player_sprite, player_rect)

        screen.blit(pokedex_button, pokedex_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()