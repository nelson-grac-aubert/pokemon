import pygame
import random

class Pokemon:
    def __init__(
        self,
        id: str,
        name: str,
        hp: int,
        attack: int,
        defense: int,
        speed: int,
        precision: int,
        types: list,
        can_evolve: bool,
        evolution_level: int,
        evolution_pokemon: list,
        level=5,
        xp=0,
        pokedex=None
    ):
        # Core data
        self.__id = id
        self.__name = name
        self.__max_hp = hp
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__speed = speed
        self.__precision = precision

        self.__types = types
        self.__can_evolve = can_evolve
        self.__evolution_level = evolution_level
        self.__evolution_pokemon = evolution_pokemon

        self.__level = 1
        self.__xp = 0

        self.__leveled_up = False
        self.__evolved = False

        self.__pokedex = pokedex

        # Apply initial level/xp
        self.set_level(level)
        self.set_xp(xp)

        # Animation data
        self.front_frames = []
        self.back_frames = []
        self.frame_index = 0
        self.frame_timer = 0
        self.frame_speed = 3
        self.scale = 1.0

    # Getters / Setters

    def get_id(self): return self.__id
    def set_id(self, v): self.__id = v

    def get_name(self): return self.__name
    def set_name(self, v): self.__name = v

    def get_max_hp(self): return self.__max_hp
    def set_max_hp(self, v): self.__max_hp = v

    def get_hp(self): return self.__hp
    def set_hp(self, v): self.__hp = v

    def get_attack(self): return self.__attack
    def set_attack(self, v): self.__attack = v

    def get_defense(self): return self.__defense
    def set_defense(self, v): self.__defense = v

    def get_speed(self): return self.__speed
    def set_speed(self, v): self.__speed = v

    def get_precision(self): return self.__precision
    def set_precision(self, v): self.__precision = v

    def get_types(self): return self.__types
    def set_types(self, v): self.__types = v

    def get_can_evolve(self): return self.__can_evolve
    def set_can_evolve(self, v): self.__can_evolve = v

    def get_evolution_level(self): return self.__evolution_level
    def set_evolution_level(self, v): self.__evolution_level = v

    def get_evolution_pokemon(self): return self.__evolution_pokemon
    def set_evolution_pokemon(self, v): self.__evolution_pokemon = v

    def get_level(self): return self.__level
    def set_level(self, v): self.__level = v

    def get_xp(self): return self.__xp
    def set_xp(self, v): self.__xp = v

    def has_leveled_up(self): return self.__leveled_up
    def has_evolved(self): return self.__evolved
    def reset_flags(self):
        self.__leveled_up = False
        self.__evolved = False

    # XP / Leveling

    def gain_xp(self, amount):
        self.set_xp(self.get_xp() + amount)
        self.check_levelup()

    def xp_required_for_level(self, level):
        return 20 + level * 5

    def check_levelup(self):
        while self.get_xp() >= self.xp_required_for_level(self.get_level()):
            self.set_xp(self.get_xp() - self.xp_required_for_level(self.get_level()))
            self.level_up()

    def level_up(self):
        self.__leveled_up = True

        self.set_level(self.get_level() + 1)
        self.set_max_hp(self.get_max_hp() + max(1, self.get_max_hp() // 20))
        self.set_hp(self.get_max_hp())
        self.set_attack(self.get_attack() + max(1, self.get_attack() // 20))
        self.set_defense(self.get_defense() + max(1, self.get_defense() // 20))
        self.set_speed(self.get_speed() + max(1, self.get_speed() // 20))

        self.evolve()

    # Evolution

    def evolve(self):
        if not self.get_can_evolve():
            return None

        if self.get_level() < self.get_evolution_level():
            return None

        evo_ids = self.get_evolution_pokemon()
        if not evo_ids:
            return None

        evo_id = evo_ids[0] if len(evo_ids) == 1 else random.choice(evo_ids)

        self.__evolved = True

        from scripts.classes.Pokedex_class import kanto_pokedex
        return kanto_pokedex.get_pokemon_by_id(evo_id)
