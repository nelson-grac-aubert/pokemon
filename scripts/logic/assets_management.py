from PIL import Image
import os
import sys
import pygame

def resource_path(relative_path: str) -> str:
    """ Returns absolute path to an asset, PyInstaller compatible.
    - Uses normal path in IDE use
    - Uses MEIPASS in .exe build """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def load_image(path: str) -> pygame.Surface:
    """ Load an image through resource_path
        convert_alpha for a transparent background .png """
    full_path = resource_path(path)
    try:
        image = pygame.image.load(full_path)
        return image.convert_alpha()
    except Exception as e:
        raise FileNotFoundError(f"Can't load image : {full_path}\n{e}")


def load_gif(path: str, size: tuple[int, int] | None = None) -> list[pygame.Surface]:
    """ Load all frames of a gif through ressource_path, PyInstaller compatible """
    full_path = resource_path(path)
    pil_img = Image.open(full_path)

    frames = []
    try:
        while True:
            frame = pil_img.convert("RGBA")

            if size is not None:
                frame = frame.resize(size, Image.NEAREST)

            mode = frame.mode
            data = frame.tobytes()
            surface = pygame.image.fromstring(data, frame.size, mode)
            frames.append(surface)

            pil_img.seek(pil_img.tell() + 1)
    except EOFError:
        pass

    return frames



def load_music(path: str) -> None:
    """ Load music through resource_path """
    full_path = resource_path(path)
    try:
        pygame.mixer.music.load(full_path)
    except Exception as e:
        raise FileNotFoundError(f"Can't load music : {full_path}\n{e}")


def load_sound(path: str) -> pygame.mixer.Sound:
    """ Load sound through resource_path """
    full_path = resource_path(path)
    try:
        return pygame.mixer.Sound(full_path)
    except Exception as e:
        raise FileNotFoundError(f"Can't load sound : {full_path}\n{e}")


def load_font(path: str, size: int) -> pygame.font.Font:
    """ Load font through resource_path """
    full_path = resource_path(path)
    try:
        return pygame.font.Font(full_path, size)
    except Exception as e:
        raise FileNotFoundError(f"Can't load font : {full_path}\n{e}")
    
def draw_music_button(screen, music_muted, music_image, music_muted_image, rect):
    """ Draw music on/off button """

    screen.blit(music_muted_image if music_muted else music_image, rect)

def draw_sound_button(screen, sound_muted, sound_mute_icon, sound_unmute_icon, rect):
    """ Draw sound on/off button """
    screen.blit(sound_mute_icon if sound_muted else sound_unmute_icon, rect)


def button_music_click(event, rect, music_muted):
    """ Mute/unmute music behavior """

    if event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(event.pos):
        music_muted = not music_muted
        if music_muted:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
    return music_muted

def button_sound_click(event, rect, sound_muted):
    """ Mute/unmute sound behavior """

    if event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(event.pos):
        sound_muted = not sound_muted
    return sound_muted
    
