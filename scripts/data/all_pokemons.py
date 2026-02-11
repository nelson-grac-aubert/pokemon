from scripts.classes.Pokemon_class import Pokemon
from scripts.data.all_types import *

# Pokemon stats are simplified using a re-usable stat template 
precision_template = {
    85:   85,        # First evolution, weak
    90:    90,        # First evolution, a bit stronger
    92:92,        # Middle evolution
    98:       95,        # Final evolution
    98:        98,        # Weak but fast pokemon, often attacks first
    88:        88,        # Tanky pokemon, slow but healthy
    100:      100,   # Mew, Mewtwo, 3 legendary birds
}

def make_pokemon(pid: str, name: str, types: list, stats: tuple) -> Pokemon:
    """
    :param stats: tuple (hp, atk, df, spd, prec, key)
    """
    hp, atk, df, spd, key = stats
    prec = precision_template[key]

    return Pokemon(name, hp, atk, df, spd, prec, types, pid)


# Instantiate all Pokemons of the first generation 

bulbasaur   = make_pokemon("001", "Bulbasaur",      [grass, poison], (45, 49, 49, 45, 90))
ivysaur     = make_pokemon("002", "Ivysaur",        [grass, poison], (60, 62, 63, 60, 92))
venusaur    = make_pokemon("003", "Venusaur",       [grass, poison], (80, 82, 83, 80, 98))

charmander  = make_pokemon("004", "Charmander",     [fire],          (39, 52, 43, 65, 90))
charmeleon  = make_pokemon("005", "Charmeleon",     [fire],          (58, 64, 58, 80, 92))
charizard   = make_pokemon("006", "Charizard",      [fire, flying],  (78, 84, 78, 100, 98))

squirtle    = make_pokemon("007", "Squirtle",       [water],         (44, 48, 65, 43, 90))
wartortle   = make_pokemon("008", "Wartortle",      [water],         (59, 63, 80, 58, 92))
blastoise   = make_pokemon("009", "Blastoise",      [water],         (79, 83, 100, 78, 98))

caterpie    = make_pokemon("010", "Caterpie",       [bug],           (45, 30, 35, 45, 85))
metapod     = make_pokemon("011", "Metapod",        [bug],           (50, 20, 55, 30, 85))
butterfree  = make_pokemon("012", "Butterfree",     [bug, flying],   (60, 45, 50, 70, 98))

weedle      = make_pokemon("013", "Weedle",         [bug, poison],   (40, 35, 30, 50, 85))
kakuna      = make_pokemon("014", "Kakuna",         [bug, poison],   (45, 25, 50, 35, 85))
beedrill    = make_pokemon("015", "Beedrill",       [bug, poison],   (65, 90, 40, 75, 98))

pidgey      = make_pokemon("016", "Pidgey",         [normal, flying],(40, 45, 40, 56, 85))
pidgeotto   = make_pokemon("017", "Pidgeotto",      [normal, flying],(63, 60, 55, 71, 92))
pidgeot     = make_pokemon("018", "Pidgeot",        [normal, flying],(83, 80, 75, 101, 98))

rattata     = make_pokemon("019", "Rattata",        [normal],        (30, 56, 35, 72, 85))
raticate    = make_pokemon("020", "Raticate",       [normal],        (55, 81, 60, 97, 90))

spearow     = make_pokemon("021", "Spearow",        [normal, flying],(40, 60, 30, 70, 85))
fearow      = make_pokemon("022", "Fearow",         [normal, flying],(65, 90, 65, 100, 98))

ekans       = make_pokemon("023", "Ekans",          [poison],        (35, 60, 44, 55, 90))
arbok       = make_pokemon("024", "Arbok",          [poison],        (60, 95, 69, 80, 90))

pikachu     = make_pokemon("025", "Pikachu",        [electric],      (35, 55, 40, 90, 98))
raichu      = make_pokemon("026", "Raichu",         [electric],      (60, 90, 55, 110, 98))

sandshrew   = make_pokemon("027", "Sandshrew",      [ground],        (50, 75, 85, 40, 90))
sandslash   = make_pokemon("028", "Sandslash",      [ground],        (75, 100, 110, 65, 90))

nidoran_f   = make_pokemon("029", "Nidoran♀",       [poison],        (55, 47, 52, 41, 90))
nidorina    = make_pokemon("030", "Nidorina",       [poison],        (70, 62, 67, 56, 92))
nidoqueen   = make_pokemon("031", "Nidoqueen",      [poison, ground],(90, 92, 87, 76, 98))

nidoran_m   = make_pokemon("032", "Nidoran♂",       [poison],        (46, 57, 40, 50, 90))
nidorino    = make_pokemon("033", "Nidorino",       [poison],        (61, 72, 57, 65, 92))
nidoking    = make_pokemon("034", "Nidoking",       [poison, ground],(81, 102, 77, 85, 98))

clefairy    = make_pokemon("035", "Clefairy",       [fairy],         (70, 45, 48, 35, 90))
clefable    = make_pokemon("036", "Clefable",       [fairy],         (95, 70, 73, 60, 98))

vulpix      = make_pokemon("037", "Vulpix",         [fire],          (38, 41, 40, 65, 90))
ninetales   = make_pokemon("038", "Ninetales",      [fire],          (73, 76, 75,100, 98))

jigglypuff  = make_pokemon("039", "Jigglypuff",     [normal, fairy], (115, 45, 20, 20, 90))
wigglytuff  = make_pokemon("040", "Wigglytuff",     [normal, fairy], (140, 70, 45, 45, 98))

zubat       = make_pokemon("041", "Zubat",          [poison, flying],(40, 45, 35, 55, 85))
golbat      = make_pokemon("042", "Golbat",         [poison, flying],(75, 80, 70, 90, 90))

oddish      = make_pokemon("043", "Oddish",         [grass, poison], (45, 50, 55, 30, 90))
gloom       = make_pokemon("044", "Gloom",          [grass, poison], (60, 65, 70, 40, 92))
vileplume   = make_pokemon("045", "Vileplume",      [grass, poison], (75, 80, 85, 50, 98))

paras       = make_pokemon("046", "Paras",          [bug, grass],    (35, 70, 55, 25, 90))
parasect    = make_pokemon("047", "Parasect",       [bug, grass],    (60, 95, 80, 30, 90))

venonat     = make_pokemon("048", "Venonat",        [bug, poison],   (60, 55, 50, 45, 90))
venomoth    = make_pokemon("049", "Venomoth",       [bug, poison],   (70, 65, 60, 90, 98))

diglett     = make_pokemon("050", "Diglett",        [ground],        (10, 55, 25, 95, 98))
dugtrio     = make_pokemon("051", "Dugtrio",        [ground],        (35,100, 50, 120, 98))

meowth      = make_pokemon("052", "Meowth",         [normal],        (40, 45, 35, 90, 90))
persian     = make_pokemon("053", "Persian",        [normal],        (65, 70, 60, 115, 98))

psyduck     = make_pokemon("054", "Psyduck",        [water],         (50, 52, 48, 55, 90))
golduck     = make_pokemon("055", "Golduck",        [water],         (80, 82, 78, 85, 90))

mankey      = make_pokemon("056", "Mankey",         [fighting],      (40, 80, 35, 70, 90))
primeape    = make_pokemon("057", "Primeape",       [fighting],      (65, 105, 60, 95, 90))

growlithe   = make_pokemon("058", "Growlithe",      [fire],          (55, 70, 45, 60, 90))
arcanine    = make_pokemon("059", "Arcanine",       [fire],          (90, 110, 80, 95, 98))

poliwag     = make_pokemon("060", "Poliwag",        [water],         (40, 50, 40, 90, 90))
poliwhirl   = make_pokemon("061", "Poliwhirl",      [water],         (65, 65, 65, 90, 92))
poliwrath   = make_pokemon("062", "Poliwrath",      [water, fighting],(90, 95, 95, 70, 98))

abra        = make_pokemon("063", "Abra",           [psychic],       (25, 20, 15, 90, 85))
kadabra     = make_pokemon("064", "Kadabra",        [psychic],       (40, 35, 30, 105, 92))
alakazam    = make_pokemon("065", "Alakazam",       [psychic],       (55, 50, 45, 120, 98))

machop      = make_pokemon("066", "Machop",         [fighting],      (70, 80, 50, 35, 90))
machoke     = make_pokemon("067", "Machoke",        [fighting],      (80, 100, 70, 45, 92))
machamp     = make_pokemon("068", "Machamp",        [fighting],      (90, 130, 80, 55, 98))

bellsprout  = make_pokemon("069", "Bellsprout",     [grass, poison], (50, 75, 35, 40, 90))
weepinbell  = make_pokemon("070", "Weepinbell",     [grass, poison], (65, 90, 50, 55, 92))
victreebel  = make_pokemon("071", "Victreebel",     [grass, poison], (80, 105, 65, 70, 98))

tentacool   = make_pokemon("072", "Tentacool",      [water, poison], (40, 40, 35, 70, 90))
tentacruel  = make_pokemon("073", "Tentacruel",     [water, poison], (80, 70, 65, 100, 90))

geodude     = make_pokemon("074", "Geodude",        [rock, ground],  (40, 80, 100, 20, 88))
graveler    = make_pokemon("075", "Graveler",       [rock, ground],  (55, 95, 115, 35, 88))
golem       = make_pokemon("076", "Golem",          [rock, ground],  (80, 120, 130, 45, 88))

ponyta      = make_pokemon("077", "Ponyta",         [fire],          (50, 85, 55, 90, 98))
rapidash    = make_pokemon("078", "Rapidash",       [fire],          (65, 100, 70, 105, 98))

slowpoke    = make_pokemon("079", "Slowpoke",       [water, psychic],(90, 65, 65, 15, 90))
slowbro     = make_pokemon("080", "Slowbro",        [water, psychic],(95, 75, 110, 30, 88))

magnemite   = make_pokemon("081", "Magnemite",      [electric, steel],(25, 35, 70, 45, 90))
magneton    = make_pokemon("082", "Magneton",       [electric, steel],(50, 60, 95, 70, 90))

farfetchd   = make_pokemon("083", "Farfetch'd",     [normal, flying],(52, 90, 55, 60, 90))

doduo       = make_pokemon("084", "Doduo",          [normal, flying],(35, 85, 45, 75, 90))
dodrio      = make_pokemon("085", "Dodrio",         [normal, flying],(60, 110, 70, 110, 98))

seel        = make_pokemon("086", "Seel",           [water],         (65, 45, 55, 45, 90))
dewgong     = make_pokemon("087", "Dewgong",        [water, ice],    (90, 70, 80, 70, 90))

grimer      = make_pokemon("088", "Grimer",         [poison],        (80, 80, 50, 25, 90))
muk         = make_pokemon("089", "Muk",            [poison],        (105, 105, 75, 50, 88))

shellder    = make_pokemon("090", "Shellder",       [water],         (30, 65, 100, 40, 90))
cloyster    = make_pokemon("091", "Cloyster",       [water, ice],    (50, 95, 180, 70, 88))

gastly      = make_pokemon("092", "Gastly",         [ghost, poison], (30, 35, 30, 80, 90))
haunter     = make_pokemon("093", "Haunter",        [ghost, poison], (45, 50, 45, 95, 92))
gengar      = make_pokemon("094", "Gengar",         [ghost, poison], (60, 65, 60, 110, 98))

onix        = make_pokemon("095", "Onix",           [rock, ground],  (35, 45, 160, 70, 88))

drowzee     = make_pokemon("096", "Drowzee",        [psychic],       (60, 48, 45, 42, 90))
hypno       = make_pokemon("097", "Hypno",          [psychic],       (85, 73, 70, 67, 90))

krabby      = make_pokemon("098", "Krabby",         [water],         (30, 105, 90, 50, 90))
kingler     = make_pokemon("099", "Kingler",        [water],         (55, 130, 115, 75, 90))

voltorb     = make_pokemon("100", "Voltorb",        [electric],      (40, 30, 50, 100, 98))
electrode   = make_pokemon("101", "Electrode",      [electric],      (60, 50, 70, 150, 98))

exeggcute   = make_pokemon("102", "Exeggcute",      [grass, psychic],(60, 40, 80, 40, 90))
exeggutor   = make_pokemon("103", "Exeggutor",      [grass, psychic],(95, 95, 85, 55, 98))

cubone      = make_pokemon("104", "Cubone",         [ground],        (50, 50, 95, 35, 90))
marowak     = make_pokemon("105", "Marowak",        [ground],        (60, 80, 110, 45, 90))

hitmonlee   = make_pokemon("106", "Hitmonlee",      [fighting],      (50, 120, 53, 87, 90))
hitmonchan  = make_pokemon("107", "Hitmonchan",     [fighting],      (50, 105, 79, 76, 90))

lickitung   = make_pokemon("108", "Lickitung",      [normal],        (90, 55, 75, 30, 90))

koffing     = make_pokemon("109", "Koffing",        [poison],        (40, 65, 95, 35, 90))
weezing     = make_pokemon("110", "Weezing",        [poison],        (65, 90, 120, 60, 88))

rhyhorn     = make_pokemon("111", "Rhyhorn",        [ground, rock],  (80, 85, 95, 25, 88))
rhydon      = make_pokemon("112", "Rhydon",         [ground, rock],  (105, 130, 120, 40, 88))

chansey     = make_pokemon("113", "Chansey",        [normal],        (250, 5, 5, 50, 88))

tangela     = make_pokemon("114", "Tangela",        [grass],         (65, 55, 115, 60, 90))

kangaskhan  = make_pokemon("115", "Kangaskhan",     [normal],        (105, 95, 80, 90, 90))

horsea      = make_pokemon("116", "Horsea",         [water],         (30, 40, 70, 60, 90))
seadra      = make_pokemon("117", "Seadra",         [water],         (55, 65, 95, 85, 90))

goldeen     = make_pokemon("118", "Goldeen",        [water],         (45, 67, 60, 63, 90))
seaking     = make_pokemon("119", "Seaking",        [water],         (80, 92, 65, 68, 90))

staryu      = make_pokemon("120", "Staryu",         [water],         (30, 45, 55, 85, 98))
starmie     = make_pokemon("121", "Starmie",        [water, psychic],(60, 75, 85, 115, 98))

mr_mime     = make_pokemon("122", "Mr. Mime",       [psychic, fairy],(40, 45, 65, 90, 90))

scyther     = make_pokemon("123", "Scyther",        [bug, flying],   (70, 110, 80, 105, 98))

jynx        = make_pokemon("124", "Jynx",           [ice, psychic],  (65, 50, 35, 95, 90))

electabuzz  = make_pokemon("125", "Electabuzz",     [electric],      (65, 83, 57, 105, 90))
magmar      = make_pokemon("126", "Magmar",         [fire],          (65, 95, 57, 93, 90))

pinsir      = make_pokemon("127", "Pinsir",         [bug],           (65, 125, 100, 85, 90))

tauros      = make_pokemon("128", "Tauros",         [normal],        (75, 100, 95, 110, 98))

magikarp    = make_pokemon("129", "Magikarp",       [water],         (20, 10, 55, 80, 85))
gyarados    = make_pokemon("130", "Gyarados",       [water, flying], (95, 125, 79, 81, 98))

lapras      = make_pokemon("131", "Lapras",         [water, ice],    (130, 85, 80, 60, 98))

ditto       = make_pokemon("132", "Ditto",          [normal],        (48, 48, 48, 48, 90))

eevee       = make_pokemon("133", "Eevee",          [normal],        (55, 55, 50, 55, 90))
vaporeon    = make_pokemon("134", "Vaporeon",       [water],         (130, 65, 60, 65, 98))
jolteon     = make_pokemon("135", "Jolteon",        [electric],      (65, 65, 60, 130, 98))
flareon     = make_pokemon("136", "Flareon",        [fire],          (65, 130, 60, 65, 98))

porygon     = make_pokemon("137", "Porygon",        [normal],        (65, 60, 70, 40, 90))

omanyte     = make_pokemon("138", "Omanyte",        [rock, water],   (35, 40, 100, 35, 90))
omastar     = make_pokemon("139", "Omastar",        [rock, water],   (70, 60, 125, 55, 88))

kabuto      = make_pokemon("140", "Kabuto",         [rock, water],   (30, 80, 90, 55, 90))
kabutops    = make_pokemon("141", "Kabutops",       [rock, water],   (60, 115, 105, 80, 90))

aerodactyl  = make_pokemon("142", "Aerodactyl",     [rock, flying],  (80, 105, 65, 130, 98))

snorlax     = make_pokemon("143", "Snorlax",        [normal],        (160, 110, 65, 30, 88))

articuno    = make_pokemon("144", "Articuno",       [ice, flying],   (90, 85, 100, 85, 100))
zapdos      = make_pokemon("145", "Zapdos",         [electric, flying],(90, 90, 85, 100, 100))
moltres     = make_pokemon("146", "Moltres",        [fire, flying],  (90, 100, 90, 90, 100))

dratini     = make_pokemon("147", "Dratini",        [dragon],        (41, 64, 45, 50, 90))
dragonair   = make_pokemon("148", "Dragonair",      [dragon],        (61, 84, 65, 70, 92))
dragonite   = make_pokemon("149", "Dragonite",      [dragon, flying],(91, 134, 95, 80, 98))

mewtwo      = make_pokemon("150", "Mewtwo",         [psychic],       (106, 110, 90, 130,100))
mew         = make_pokemon("151", "Mew",            [psychic],       (100, 100,	100, 100, 100))


espeon      = make_pokemon("196", "Espeon",         [psychic],       (65, 65, 60, 110, 98))
umbreon      = make_pokemon("197", "Umbreon",         [dark],       (95, 65, 110, 65, 88))

leafeon      = make_pokemon("470", "Leafeon",         [grass],       (65, 110, 130, 95, 98))
glaceon      = make_pokemon("471", "Glaceon",         [ice],       (65, 60, 110, 65, 98))

Sylveon      = make_pokemon("700", "Sylveon",         [fairy],       (95, 65, 65, 60, 98))

kanto_pokemons = [
    bulbasaur, ivysaur, venusaur,charmander, charmeleon, charizard,squirtle, wartortle, blastoise,
    caterpie, metapod, butterfree,weedle, kakuna, beedrill,pidgey, pidgeotto, pidgeot,rattata, raticate,
    spearow, fearow,ekans, arbok,pikachu, raichu,sandshrew, sandslash,nidoran_f, nidorina, nidoqueen,
    nidoran_m, nidorino, nidoking,clefairy, clefable,vulpix, ninetales,jigglypuff, wigglytuff,zubat, golbat,
    oddish, gloom, vileplume,paras, parasect,venonat, venomoth,diglett, dugtrio,meowth, persian,
    psyduck, golduck,mankey, primeape,growlithe, arcanine,poliwag, poliwhirl, poliwrath,abra, kadabra, alakazam,
    machop, machoke, machamp,bellsprout, weepinbell, victreebel,tentacool, tentacruel,geodude, graveler, golem,
    ponyta, rapidash,slowpoke, slowbro,magnemite, magneton,farfetchd,doduo, dodrio,seel, dewgong,grimer, muk,
    shellder, cloyster,gastly, haunter, gengar,onix,drowzee, hypno,krabby, kingler,voltorb, electrode,
    exeggcute, exeggutor,cubone, marowak,hitmonlee, hitmonchan,lickitung,koffing, weezing,rhyhorn, rhydon,chansey,
    tangela,kangaskhan,horsea, seadra,goldeen, seaking,staryu, starmie,mr_mime,scyther,jynx,electabuzz,magmar,
    pinsir, tauros, magikarp, gyarados, lapras, ditto, eevee, vaporeon, jolteon, flareon, porygon, omanyte, omastar, kabuto, 
    kabutops, aerodactyl, snorlax, articuno, zapdos, moltres, dratini, dragonair, dragonite, mewtwo, mew]
