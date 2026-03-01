import pygame
from scripts.classes.PokemonDisplay_class import PokemonDisplay
from scripts.classes.Pokedex_class import Pokedex
from scripts.classes.PlayerPokedex_class import PlayerPokedex
from scripts.logic.assets_management import load_font, load_image
from scripts.logic.overworld_game_loop import overworld_game_loop

# Dialog box settings
DIALOG_FONT_SIZE = 26
BOX_HEIGHT = 140
TEXT_MARGIN = 20

def draw_dialog_box(screen, font, text):
    """Draws a dialog box with wrapped text."""
    width, height = screen.get_size()
    box_rect = pygame.Rect(0, height - BOX_HEIGHT, width, BOX_HEIGHT)

    # Background box
    pygame.draw.rect(screen, (255, 255, 255), box_rect)
    pygame.draw.rect(screen, (0, 0, 0), box_rect, 4)

    # Text rendering (simple wrap)
    words = text.split(" ")
    lines = []
    current = ""

    for w in words:
        test = current + w + " "
        if font.size(test)[0] < width - TEXT_MARGIN * 2:
            current = test
        else:
            lines.append(current)
            current = w + " "
    lines.append(current)

    # Draw lines
    y = height - BOX_HEIGHT + TEXT_MARGIN
    for line in lines:
        surf = font.render(line, True, (0, 0, 0))
        screen.blit(surf, (TEXT_MARGIN, y))
        y += font.get_height() + 4

def wait_for_click():
    """Waits until the player clicks to continue."""
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                waiting = False

def run_game_intro(screen, clock, pokedex):
    """Runs the intro sequence and returns the chosen starter Pokémon."""
    width, height = screen.get_size()

    # Load Pokémon font
    font = load_font("assets/font/Pokemon_GB.ttf", DIALOG_FONT_SIZE)

    # Load background image
    # background = load_image("assets/images/forest_background.jpg")
    background = load_image("assets/images/professors_1.png")
    background = pygame.transform.scale(background, (width, height))

    dialogs = [
        "Pr. Pellat : Hello, and welcome to Kanto, the best region of the Pokémon universe!",
        "Pr. Sandoval : Maybe you've seen our fully completed Pokédex on the main screen.",
        "Pr. Grac-Aubert : Your goal in this game is to catch them all, and complete your own Pokédex!",
        "Pr. Pellat : You will fight wild Pokémon and capture them when they faint, adding them one by one.",
        "Pr. Sandoval : There are more than 150 Pokémons to catch!",
        "Pr. Grac-Aubert : It's dangerous to go alone! Pick a starter Pokémon to begin  your adventure."
    ]

    # Dialog sequence
    for text in dialogs:
        screen.blit(background, (0, -50))  # Draw background
        draw_dialog_box(screen, font, text)
        pygame.display.flip()
        wait_for_click()

    # Starter selection
    starters_id = [0, 3, 6]  # Bulbasaur, Charmander, Squirtle

    starter_displays = []
    starters_y_position = height // 2 + 50
    positions = [(width // 4, starters_y_position), (width // 2, starters_y_position), (3 * width // 4, starters_y_position)]

    for idx, pos in zip(starters_id, positions):
        p = PokemonDisplay(pokedex.get_pokemons()[idx], scale=3.0, is_front=True)
        p.set_position(pos[0], pos[1])
        starter_displays.append(p)

    choosing = True
    chosen_pokemon = None

    while choosing:
        background = load_image("assets/images/starter_background.png")
        background = pygame.transform.scale(background, (width, height))
        screen.blit(background, (0, 0))  # Draw background

        # Draw starters
        for p in starter_displays:
            p.update()
            p.draw(screen)

        draw_dialog_box(screen, font, "Click on a starter to choose it.")
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for p in starter_displays:
                    if p.rect.collidepoint(mx, my):
                        chosen_pokemon = p.pokemon
                        choosing = False

        clock.tick(60)

    # Create player pokedex with starter
    new_pokedex = PlayerPokedex()
    new_pokedex.set_pokemons([])
    new_pokedex.add_pokemon(chosen_pokemon)
    new_pokedex.choose_as_combat_pokemon(chosen_pokemon)

    overworld_game_loop(screen, clock, new_pokedex)

    return new_pokedex