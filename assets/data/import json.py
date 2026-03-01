import json

with open("all_pokemons.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for p in data["pokemons"]:
    p["level"] = 5
    p["xp"] = 0

with open("pokemons_updated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)