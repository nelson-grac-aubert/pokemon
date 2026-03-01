import pygame
import random
from scripts.classes.PokemonDisplay_class import PokemonDisplay

class EvolutionScreen:
    def __init__(self, screen, old_pokemon, new_pokemon):
        self.screen = screen

        self.old_display = PokemonDisplay(old_pokemon, scale=4, is_front=True)
        self.new_display = PokemonDisplay(new_pokemon, scale=4, is_front=True)

        w, h = screen.get_size()
        self.center_x = w // 2
        self.center_y = h // 2

        self.old_display.set_position(self.center_x, self.center_y)
        self.new_display.set_position(self.center_x, self.center_y)

        # Animation phases
        self.phase = "alternate"
        self.timer = 0

        # Alternance
        self.alt_speed = 40
        self.alt_timer = 0
        self.show_old = True
        self.min_alt_speed = 10 

        # Flash
        self.flash_alpha = 0

        # Durations
        self.alternate_duration = 240   
        self.flash_duration = 20       
        self.final_duration = 90   

        # Final pulse
        self.pulse_scale = 3.0
        self.pulse_direction = 1

    def update(self):
        self.timer += 1

        # Alternate pokemon and its evolution
        if self.phase == "alternate":
            self.alt_timer += 1

            if self.alt_timer >= self.alt_speed:
                self.alt_timer = 0
                self.show_old = not self.show_old

                if self.alt_speed > self.min_alt_speed:
                    self.alt_speed -= 1

            if self.timer >= self.alternate_duration:
                self.phase = "flash"
                self.timer = 0

        # White flash
        elif self.phase == "flash":
            self.flash_alpha += 25
            if self.flash_alpha >= 255:
                self.phase = "final"
                self.timer = 0

        # Final pokemon with pulse animation
        elif self.phase == "final":
            if self.pulse_direction == 1:
                self.pulse_scale += 0.02
                if self.pulse_scale >= 3.2:
                    self.pulse_direction = -1
            else:
                self.pulse_scale -= 0.02
                if self.pulse_scale <= 2.9:
                    self.pulse_direction = 1

            self.new_display.scale = self.pulse_scale

    def draw(self):

        self.screen.fill((0, 0, 0))

        if self.phase == "alternate":
            if self.show_old:
                self.old_display.update()
                self.old_display.draw(self.screen)
            else:
                self.new_display.update()
                self.new_display.draw(self.screen)

        elif self.phase == "flash":
            flash = pygame.Surface(self.screen.get_size())
            flash.fill((255, 255, 255))
            flash.set_alpha(self.flash_alpha)
            self.screen.blit(flash, (0, 0))

        elif self.phase == "final":
            self.new_display.update()
            self.new_display.draw(self.screen)

    def is_finished(self):
        return self.phase == "final" and self.timer >= self.final_duration