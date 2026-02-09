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

normal.set_weaknesses([fighting])
normal.set_strenghts([])
normal.set_useless([ghost])

fire.set_weaknesses([water, ground, rock])
fire.set_strenghts([grass, ice, bug, steel])
fire.set_useless([])

water.set_weaknesses([electric, grass])
water.set_strenghts([fire, ground, rock])
water.set_useless([])

grass.set_weaknesses([fire, ice, poison, flying, bug])
grass.set_strenghts([water, ground, rock])
grass.set_useless([])

electric.set_weaknesses([ground])
electric.set_strenghts([water, flying])
electric.set_useless([])

ice.set_weaknesses([fire, fighting, rock, steel])
ice.set_strenghts([grass, ground, flying, dragon])
ice.set_useless([])

fighting.set_weaknesses([flying, psychic, fairy])
fighting.set_strenghts([normal, ice, rock, dark, steel])
fighting.set_useless([])

poison.set_weaknesses([ground, psychic])
poison.set_strenghts([grass, fairy])
poison.set_useless([steel])

ground.set_weaknesses([water, grass, ice])
ground.set_strenghts([fire, electric, poison, rock, steel])
ground.set_useless([flying])

flying.set_weaknesses([electric, ice, rock])
flying.set_strenghts([grass, fighting, bug])
flying.set_useless([ground])

psychic.set_weaknesses([bug, ghost, dark])
psychic.set_strenghts([fighting, poison])
psychic.set_useless([dark])

bug.set_weaknesses([fire, flying, rock])
bug.set_strenghts([grass, psychic, dark])
bug.set_useless([])

rock.set_weaknesses([water, grass, fighting, ground, steel])
rock.set_strenghts([fire, ice, flying, bug])
rock.set_useless([])

ghost.set_weaknesses([ghost, dark])
ghost.set_strenghts([psychic, ghost])
ghost.set_useless([normal, fighting])

dragon.set_weaknesses([ice, dragon, fairy])
dragon.set_strenghts([dragon])
dragon.set_useless([fairy])

dark.set_weaknesses([fighting, bug, fairy])
dark.set_strenghts([psychic, ghost])
dark.set_useless([psychic])

steel.set_weaknesses([fire, fighting, ground])
steel.set_strenghts([ice, rock, fairy])
steel.set_useless([poison])

fairy.set_weaknesses([poison, steel])
fairy.set_strenghts([fighting, dragon, dark])
fairy.set_useless([dragon])