import pygame
from scripts.logic.assets_management import load_gif

class PokemonDisplay:
    def __init__(self, pokemon, scale=1.0, is_front=True):
        self.pokemon = pokemon
        self.scale = scale
        self.is_front = is_front

        self.frames = []
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_speed = 3
        
        self.x = 0
        self.y = 0

        # Animation for combat start and Pokemon fainting
        self.entry_animation = False
        self.entry_speed = 15  # à ajuster selon ton feeling
        self.final_x = 0
        self.final_y = 0
        self.current_animation = None
        self.animation_data = {}

        self.load_sprites()
        if self.frames:
            first_frame = self.frames[0]
            self.rect = first_frame.get_rect(center=(self.x, self.y))
        else:
            self.rect = pygame.Rect(0, 0, 0, 0)

    def load_sprites(self):
        """ Load sprites using pyinstaller-safe import """
        pid = self.pokemon.get_id()

        if self.is_front:
            path = f"assets/sprites/{pid}.gif"
        else:
            path = f"assets/sprites/{pid}b.gif"

        raw_frames = load_gif(path)
        self.frames = [self._scale_frame(f) for f in raw_frames]

    def update(self):
        # GIF animation
        if self.frames:
            self.frame_timer += 1
            if self.frame_timer >= self.frame_speed:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)

        # No animation active
        if self.current_animation is None:
            return

        # Combat entry animation
        if self.current_animation == "entry":
            speed = self.animation_data["speed"]

            if self.x < self.final_x:
                self.x += speed
                if self.x >= self.final_x:
                    self.x = self.final_x
                    self.current_animation = None
            elif self.x > self.final_x:
                self.x -= speed
                if self.x <= self.final_x:
                    self.x = self.final_x
                    self.current_animation = None

            self.rect.center = (self.x, self.y)

    def draw(self, surface):
        """ Draw the animated Pokemon sprite on screen"""
        if not self.frames:
            return

        frame = self.frames[self.frame_index]
        rect = frame.get_rect(center=(self.x, self.y))
        surface.blit(frame, rect)

    # Blit tools

    def set_position(self, x, y):
        self.final_x = x
        self.final_y = y
        self.x = x
        self.y = y
        self.rect.center = (x, y)

    def _scale_frame(self, frame):
        """ Use to """
        if self.scale == 1.0:
            return frame

        w = int(frame.get_width() * self.scale)
        h = int(frame.get_height() * self.scale)
        return pygame.transform.scale(frame, (w, h))
    
    def start_entry_animation(self, from_left=True, speed=4):
        """ Animate Pokémon to appear at the start of a combat """
        self.current_animation = "entry"
        self.animation_data = {
            "speed": speed,
            "from_left": from_left
        }

        # Starting position outside the screen
        if from_left:
            self.x = -200
        else:
            self.x = 1000  # à adapter à ta résolution

        self.rect.center = (self.x, self.y)
