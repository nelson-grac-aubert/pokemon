import json
import os
from scripts.logic.assets_management import resource_path
from scripts.logic.json_management import load_types_from_json, filter_pokemons_by_ids


class RegisteredPokedex:

    def __init__(self):
        self.pokemons = []          # list of Pokemon objects
        self.encounters = {}        # id -> count
        self.json_path = resource_path("assets/data/registered_pokemons.json")

        self.load_from_json()

    def register_encounter(self, pokemon, intro_mode=False):
        pid = pokemon.get_id()

        if intro_mode:
            if pid not in self.encounters or self.encounters[pid] == 0:
                self.encounters[pid] = 1
                self.pokemons.append(pokemon)
                self.save_to_json()
            return

        if pid in self.encounters:
            self.encounters[pid] += 1
        else:
            self.encounters[pid] = 1
            self.pokemons.append(pokemon)

            self.save_to_json()

    def save_to_json(self):
        data = []

        for p in self.pokemons:
            pid = p.get_id()
            data.append({
                "id": pid,
                "name": p.get_name(),
                "encounters": self.encounters.get(pid, 1)
            })

        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def load_from_json(self):
        if not os.path.exists(self.json_path):
            return

        with open(self.json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # 1. Charger les compteurs et collecter les IDs
        ids = []
        for entry in data:
            pid = entry["id"]
            count = entry["encounters"]
            self.encounters[pid] = count
            ids.append(pid)

        type_dict = load_types_from_json("assets/data/all_types.json")

        self.pokemons = filter_pokemons_by_ids(ids, type_dict)

    # Needed by PokedexDisplay_class
    def get_pokemons(self):
        return self.pokemons

    # Needed by RegisteredPokedexDisplay
    def get_encounter_count(self, pokemon):
        return self.encounters.get(pokemon.get_id(), 0)