import pygame
from scripts.classes.PokemonDisplay_class import PokemonDisplay

# Duration of the intro animation (15 seconds)
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
        p.set_position(-60, 180 + i * 150)  # Start outside the screen
        animated_pokemons.append(("right", p))

    # Create PokemonDisplay objects for legendary birds (moving right → left)
    for i, idx in enumerate(LEGENDARIES):
        p = PokemonDisplay(pokedex.get_pokemons()[idx], scale=2.0, is_front=True)
        p.set_position(width + 60, 100 + i * 160)
        animated_pokemons.append(("left", p))

    start_time = pygame.time.get_ticks()

    running = True
    while running:
        now = pygame.time.get_ticks()

        # End intro after the duration
        if now - start_time >= INTRO_DURATION:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Background color
        screen.fill((235, 235, 235))

        # Animate Pokémon movement
        for direction, poke in animated_pokemons:
            if direction == "right":
                poke.x += 1.8  # Move to the right
            else:
                poke.x -= 1.8  # Move to the left

            poke.update()
            poke.draw(screen)

        pygame.display.flip()
        clock.tick(60)