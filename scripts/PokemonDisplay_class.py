import pygame
from assets_management import load_gif

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

        self.load_sprites()

    # Load sprites

    def load_sprites(self):
        pid = self.pokemon.get_id()

        if self.is_front:
            path = f"../assets/sprites/{pid}.gif"
        else:
            path = f"../assets/sprites/{pid}_back.gif"

        raw_frames = load_gif(path)
        self.frames = [self._scale_frame(f) for f in raw_frames]

    # Animation

    def update(self):
        if not self.frames:
            return

        self.frame_timer += 1
        if self.frame_timer >= self.frame_speed:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)

    # Display
    def draw(self, surface):
        if not self.frames:
            return

        frame = self.frames[self.frame_index]
        rect = frame.get_rect(center=(self.x, self.y))
        surface.blit(frame, rect)

    # Blit tools

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def _scale_frame(self, frame):
        if self.scale == 1.0:
            return frame

        w = int(frame.get_width() * self.scale)
        h = int(frame.get_height() * self.scale)
        return pygame.transform.scale(frame, (w, h))