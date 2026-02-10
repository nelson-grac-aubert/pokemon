import json
from scripts.logic.assets_management import resource_path
from scripts.classes.Pokemon_class import Pokemon
from scripts.classes.PokemonType_class import PokemonType


def load_json(relative_path: str) -> dict:
    """Load a JSON file using a PyInstaller‑safe absolute path."""
    full_path = resource_path(relative_path)

    try:
        with open(full_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        raise FileNotFoundError(f"Unable to load JSON file: {full_path}\n{e}")


def load_types_from_json(path: str) -> dict[str, PokemonType]:
    data = load_json(path)

    raw_types = data

    # Create empty Type objects
    type_objects = {
        name: PokemonType(name, [], [], [])
        for name in raw_types.keys()
    }

    # Fill their strength, weakness, useless lists
    for name, info in raw_types.items():
        t = type_objects[name]

        # mapping
        def safe(names):
            return [type_objects[n] for n in names if n in type_objects]

        t.set_weaknesses(safe(info.get("weaknesses", [])))
        t.set_strenghts(safe(info.get("strenghts", [])))
        t.set_useless(safe(info.get("useless", [])))

    return type_objects


def load_pokemons_from_json(path: str, type_dict: dict[str, PokemonType]) -> list[Pokemon]:
    """
    Charge les Pokémon depuis un JSON et remplace les noms de types
    par les objets PokemonType correspondants.
    """

    data = load_json(path)
    pokemons = []

    for entry in data.get("pokemons", []):
        types = [type_dict[t] for t in entry["types"]]

        pokemon = Pokemon(
            name=entry["name"],
            hp=entry["hp"],
            attack=entry["attack"],
            defense=entry["defense"],
            speed=entry["speed"],
            precision=entry["precision"],
            types=types,
            id=entry["id"]
        )

        pokemons.append(pokemon)

    return pokemons