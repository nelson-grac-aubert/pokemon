from type_class import Type

normal  = Type("Normal",  [], [], [])
fire    = Type("Fire",    [], [], [])
water   = Type("Water",   [], [], [])
grass   = Type("Grass",   [], [], [])
electric= Type("Electric",[], [], [])
ice     = Type("Ice",     [], [], [])
fighting= Type("Fighting",[], [], [])
poison  = Type("Poison",  [], [], [])
ground  = Type("Ground",  [], [], [])
flying  = Type("Flying",  [], [], [])
psychic = Type("Psychic", [], [], [])
bug     = Type("Bug",     [], [], [])
rock    = Type("Rock",    [], [], [])
ghost   = Type("Ghost",   [], [], [])
dragon  = Type("Dragon",  [], [], [])
dark    = Type("Dark",    [], [], [])
steel   = Type("Steel",   [], [], [])
fairy   = Type("Fairy",   [], [], [])

normal.set_weaknesses([fighting])
normal.set_strenghts([])
normal.set_negates([ghost])

fire.set_weaknesses([water, ground, rock])
fire.set_strenghts([grass, ice, bug, steel])
fire.set_negates([])

water.set_weaknesses([electric, grass])
water.set_strenghts([fire, ground, rock])
water.set_negates([])

grass.set_weaknesses([fire, ice, poison, flying, bug])
grass.set_strenghts([water, ground, rock])
grass.set_negates([])

electric.set_weaknesses([ground])
electric.set_strenghts([water, flying])
electric.set_negates([])

ice.set_weaknesses([fire, fighting, rock, steel])
ice.set_strenghts([grass, ground, flying, dragon])
ice.set_negates([])

fighting.set_weaknesses([flying, psychic, fairy])
fighting.set_strenghts([normal, ice, rock, dark, steel])
fighting.set_negates([])

poison.set_weaknesses([ground, psychic])
poison.set_strenghts([grass, fairy])
poison.set_negates([steel])

ground.set_weaknesses([water, grass, ice])
ground.set_strenghts([fire, electric, poison, rock, steel])
ground.set_negates([flying])

flying.set_weaknesses([electric, ice, rock])
flying.set_strenghts([grass, fighting, bug])
flying.set_negates([ground])

psychic.set_weaknesses([bug, ghost, dark])
psychic.set_strenghts([fighting, poison])
psychic.set_negates([dark])

bug.set_weaknesses([fire, flying, rock])
bug.set_strenghts([grass, psychic, dark])
bug.set_negates([])

rock.set_weaknesses([water, grass, fighting, ground, steel])
rock.set_strenghts([fire, ice, flying, bug])
rock.set_negates([])

ghost.set_weaknesses([ghost, dark])
ghost.set_strenghts([psychic, ghost])
ghost.set_negates([normal, fighting])

dragon.set_weaknesses([ice, dragon, fairy])
dragon.set_strenghts([dragon])
dragon.set_negates([fairy])

dark.set_weaknesses([fighting, bug, fairy])
dark.set_strenghts([psychic, ghost])
dark.set_negates([psychic])

steel.set_weaknesses([fire, fighting, ground])
steel.set_strenghts([ice, rock, fairy])
steel.set_negates([poison])

fairy.set_weaknesses([poison, steel])
fairy.set_strenghts([fighting, dragon, dark])
fairy.set_negates([dragon])