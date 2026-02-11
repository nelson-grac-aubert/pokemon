import pygame
from scripts.logic.assets_management import load_music, load_sound

class SoundControl:
    """ Centralized control of music and sound"""

    def __init__(self):
        pygame.mixer.init()
        self.current_music = None
        self.music_queue = []
        self.sounds = {}

    # Music
    def play_music(self, path: str, volume: float = 1.0, loop: bool = True):
        """Charge et joue une musique via load_music."""
        load_music(path) 
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(-1 if loop else 0)
        self.current_music = path

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_music = None

    def pause_music(self):
        pygame.mixer.music.pause()

    def resume_music(self):
        pygame.mixer.music.unpause()

    def queue_music(self, path: str):
        """Add music to the queue"""
        self.music_queue.append(path)

    def update(self):
        """ To be called in the main loop to handle queue """
        if not pygame.mixer.music.get_busy() and self.music_queue:
            next_track = self.music_queue.pop(0)
            self.play_music(next_track)

    # Sound
    def load_sound_effect(self, name: str, path: str):
        """ Load a sound and save it with a name """
        self.sounds[name] = load_sound(path)

    def play_sound(self, name: str, volume: float = 1.0):
        """ Play an already loaded sound """
        if name not in self.sounds:
            raise KeyError(f"Sound '{name}' not loaded.")
        sound = self.sounds[name]
        sound.set_volume(volume)
        sound.play()


