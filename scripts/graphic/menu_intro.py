import pygame
from scripts.classes.PokemonDisplay_class import PokemonDisplay
from scripts.graphic.colors import BEIGE
from scripts.logic.assets_management import load_font

# Duration of the intro animation (10 seconds)
INTRO_DURATION = 10000  

def run_intro(screen, clock, pokedex):
    width, height = screen.get_size()

    # Pokémon indexes to display (must match your JSON order)
    STARTERS = [0, 3, 6]          # Example: Bulbasaur, Charmander, Squirtle
    LEGENDARIES = [143, 144, 145] # Example: Articuno, Zapdos, Moltres

    animated_pokemons = []

    # Create PokemonDisplay objects for starters (moving left → right)
    for i, idx in enumerate(STARTERS):
        p = PokemonDisplay(pokedex.get_pokemons()[idx], scale=2.0, is_front=True)
        p.set_position(-60, 180 + i * 150)
        animated_pokemons.append(("right", p))

    # Create PokemonDisplay objects for legendary birds (moving right → left)
    for i, idx in enumerate(LEGENDARIES):
        p = PokemonDisplay(pokedex.get_pokemons()[idx], scale=2.0, is_front=True)
        p.set_position(width + 60, 100 + i * 160)
        animated_pokemons.append(("left", p))

    start_time = pygame.time.get_ticks()
    skip_requested = False  # <-- NEW

    # Font for skip text
    skip_font = load_font("assets/font/Pokemon_GB.ttf", 18)

    running = True
    while running:
        now = pygame.time.get_ticks()

        # End intro after the duration OR if skip requested
        if now - start_time >= INTRO_DURATION or skip_requested:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Skip intro on click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                skip_requested = True  # <-- NEW

        # Background color
        screen.fill((BEIGE))

        # Animate Pokémon movement
        for direction, poke in animated_pokemons:
            if direction == "right":
                poke.x += 1.8
            else:
                poke.x -= 1.8

            poke.update()
            poke.draw(screen)

        # Draw "Click to skip" text
        skip_text = skip_font.render("Click to skip", True, (0, 0, 0))
        screen.blit(skip_text, (width - skip_text.get_width() - 10, height - 30))

        pygame.display.flip()
        clock.tick(60)