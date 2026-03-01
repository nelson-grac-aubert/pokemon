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

    required_keys = [
    "id", "name", "hp", "attack", "defense", "speed",
    "precision", "types", "can_evolve",
    "evolution_level", "evolution_pokemon"
]

    for entry in data.get("pokemons", []):
        for key in required_keys:
            if key not in entry:
                raise ValueError(f"Missing key '{key}' in Pokémon entry: {entry}")

        types = [type_dict[t] for t in entry["types"]]

        pokemon = Pokemon(
        id=entry["id"],
        name=entry["name"],
        hp=entry["hp"],
        attack=entry["attack"],
        defense=entry["defense"],
        speed=entry["speed"],
        precision=entry["precision"],
        types=types,
        can_evolve=entry["can_evolve"],
        evolution_level=entry["evolution_level"],
        evolution_pokemon=entry["evolution_pokemon"],
        level=entry.get("level", 5),  
        xp=entry.get("xp", 0)        
    )

        pokemons.append(pokemon)

    return pokemons

        
def filter_pokemons_by_ids(ids: list[str], type_dict: dict[str, PokemonType]) -> list[Pokemon]:
    all_pokemons = load_pokemons_from_json("assets/data/all_pokemons.json", type_dict)
    return [p for p in all_pokemons if p.get_id() in ids]

def save_pokemons_to_json(pokemons: list[Pokemon], output_path: str) -> None:
    """
    Sauvegarde une liste d'objets Pokemon dans un fichier JSON
    au même format que celui utilisé par load_pokemons_from_json().
    """

    data = {"pokemons": []}

    for p in pokemons:
        entry = {
        "id": p.get_id(),
        "name": p.get_name(),
        "hp": p.get_hp(),
        "attack": p.get_attack(),
        "defense": p.get_defense(),   
        "speed": p.get_speed(),
        "precision": p.get_precision(),
        "types": [t.get_name() for t in p.get_types()],
        "can_evolve": p.get_can_evolve(),
        "evolution_level": p.get_evolution_level(),
        "evolution_pokemon": p.get_evolution_pokemon(),
        "level": p.get_level(),       
        "xp": p.get_xp()            
    }


        data["pokemons"].append(entry)

    # Write in file
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
