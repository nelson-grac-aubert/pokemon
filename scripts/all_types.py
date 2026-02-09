from PokemonType_class import PokemonType

normal  = PokemonType("Normal",  [], [], [])
fire    = PokemonType("Fire",    [], [], [])
water   = PokemonType("Water",   [], [], [])
grass   = PokemonType("Grass",   [], [], [])
electric= PokemonType("Electric",[], [], [])
ice     = PokemonType("Ice",     [], [], [])
fighting= PokemonType("Fighting",[], [], [])
poison  = PokemonType("Poison",  [], [], [])
ground  = PokemonType("Ground",  [], [], [])
flying  = PokemonType("Flying",  [], [], [])
psychic = PokemonType("Psychic", [], [], [])
bug     = PokemonType("Bug",     [], [], [])
rock    = PokemonType("Rock",    [], [], [])
ghost   = PokemonType("Ghost",   [], [], [])
dragon  = PokemonType("Dragon",  [], [], [])
dark    = PokemonType("Dark",    [], [], [])
steel   = PokemonType("Steel",   [], [], [])
fairy   = PokemonType("Fairy",   [], [], [])

normal.set_weaknesses([rock, steel])
normal.set_strenghts([])
normal.set_useless([ghost])

fire.set_weaknesses([fire ,water, rock, dragon])
fire.set_strenghts([grass, ice, bug, steel])
fire.set_useless([])

water.set_weaknesses([water, grass, dragon])
water.set_strenghts([fire, ground, rock])
water.set_useless([])

grass.set_weaknesses([fire, grass, poison, flying, bug, dragon, steel])
grass.set_strenghts([water, ground, rock])
grass.set_useless([])

electric.set_weaknesses([grass, electric, dragon])
electric.set_strenghts([water, flying])
electric.set_useless([ground])

ice.set_weaknesses([fire, water, ice, steel])
ice.set_strenghts([grass, ground, flying, dragon])
ice.set_useless([])

fighting.set_weaknesses([poison, flying, psychic, bug, fairy])
fighting.set_strenghts([normal, ice, rock, dark, steel])
fighting.set_useless([ghost])

poison.set_weaknesses([poison, ground, rock, ghost])
poison.set_strenghts([grass, fairy])
poison.set_useless([steel])

ground.set_weaknesses([grass, bug])
ground.set_strenghts([fire, electric, poison, rock, steel])
ground.set_useless([flying])

flying.set_weaknesses([electric, rock, steel])
flying.set_strenghts([grass, fighting, bug])
flying.set_useless([])

psychic.set_weaknesses([psychic, steel])
psychic.set_strenghts([fighting, poison])
psychic.set_useless([dark])

bug.set_weaknesses([fire, fighting, poison, flying, ghost, steel, fairy])
bug.set_strenghts([grass, psychic, dark])
bug.set_useless([])

rock.set_weaknesses([fighting, ground, steel])
rock.set_strenghts([fire, ice, flying, bug])
rock.set_useless([])

ghost.set_weaknesses([dark])
ghost.set_strenghts([psychic, ghost])
ghost.set_useless([normal])

dragon.set_weaknesses([steel])
dragon.set_strenghts([dragon])
dragon.set_useless([fairy])

dark.set_weaknesses([fighting, dark, fairy])
dark.set_strenghts([psychic, ghost])
dark.set_useless([])

steel.set_weaknesses([fire, water, electric, steel])
steel.set_strenghts([ice, rock, fairy])
steel.set_useless([])

fairy.set_weaknesses([fire, poison, steel])
fairy.set_strenghts([fighting, dragon, dark])
fairy.set_useless([])