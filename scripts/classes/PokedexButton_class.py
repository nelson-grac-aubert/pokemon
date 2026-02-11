import pygame
from scripts.logic.assets_management import load_image

class PokedexButton:
    def __init__(self) : 
        self.__img = load_image("assets/images/pokedex.png").convert_alpha()
        self.__img = pygame.transform.scale(self.img, (140, 120))  # adapte la taille 
        self.__img_rect = self.img.get_rect()
        self.__img_rect.topright = (780, 20)  # position en haut à droite
        self.__hover_scale = 1.0
        self.__target_scale = 1.0
        self.__button_click_cooldown = 0