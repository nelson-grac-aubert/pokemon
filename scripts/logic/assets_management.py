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
    
