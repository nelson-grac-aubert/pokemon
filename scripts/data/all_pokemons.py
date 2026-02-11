from scripts.classes.Pokemon_class import Pokemon
from scripts.data.all_types import *

# Pokemon stats are simplified using a re-usable stat template 
precision_template = {
    "base_weak":   85,        # First evolution, weak
    "base_mid":    90,        # First evolution, a bit stronger
    "intermediate":92,        # Middle evolution
    "final":       95,        # Final evolution
    "fast":        98,        # Weak but fast pokemon, often attacks first
    "tank":        88,        # Tanky pokemon, slow but healthy
    "legend":      100,   # Mew, Mewtwo, 3 legendary birds
}

def make_pokemon(pid: str, name: str, types: list, stats: tuple) -> Pokemon:
    """
    :param stats: tuple (hp, atk, df, spd, prec, key)
    """
    hp, atk, df, spd, key = stats
    prec = precision_template[key]

    return Pokemon(name, hp, atk, df, spd, prec, types, pid)


# Instantiate all Pokemons of the first generation 

bulbasaur   = make_pokemon("001", "Bulbasaur",      [grass, poison], (45, 49, 49, 45, "base_mid"))
ivysaur     = make_pokemon("002", "Ivysaur",        [grass, poison], (60, 62, 63, 60, "intermediate"))
venusaur    = make_pokemon("003", "Venusaur",       [grass, poison], (80, 82, 83, 80, "final"))

charmander  = make_pokemon("004", "Charmander",     [fire],          (39, 52, 43, 65, "base_mid"))
charmeleon  = make_pokemon("005", "Charmeleon",     [fire],          (58, 64, 58, 80, "intermediate"))
charizard   = make_pokemon("006", "Charizard",      [fire, flying],  (78, 84, 78, 100, "final"))

squirtle    = make_pokemon("007", "Squirtle",       [water],         (44, 48, 65, 43, "base_mid"))
wartortle   = make_pokemon("008", "Wartortle",      [water],         (59, 63, 80, 58, "intermediate"))
blastoise   = make_pokemon("009", "Blastoise",      [water],         (79, 83, 100, 78, "final"))

caterpie    = make_pokemon("010", "Caterpie",       [bug],           (45, 30, 35, 45, "base_weak"))
metapod     = make_pokemon("011", "Metapod",        [bug],           (50, 20, 55, 30, "base_weak"))
butterfree  = make_pokemon("012", "Butterfree",     [bug, flying],   (60, 45, 50, 70, "fast"))

weedle      = make_pokemon("013", "Weedle",         [bug, poison],   (40, 35, 30, 50, "base_weak"))
kakuna      = make_pokemon("014", "Kakuna",         [bug, poison],   (45, 25, 50, 35, "base_weak"))
beedrill    = make_pokemon("015", "Beedrill",       [bug, poison],   (65, 90, 40, 75, "fast"))

pidgey      = make_pokemon("016", "Pidgey",         [normal, flying],(40, 45, 40, 56, "base_weak"))
pidgeotto   = make_pokemon("017", "Pidgeotto",      [normal, flying],(63, 60, 55, 71, "intermediate"))
pidgeot     = make_pokemon("018", "Pidgeot",        [normal, flying],(83, 80, 75, 101, "fast"))

rattata     = make_pokemon("019", "Rattata",        [normal],        (30, 56, 35, 72, "base_weak"))
raticate    = make_pokemon("020", "Raticate",       [normal],        (55, 81, 60, 97, "base_mid"))

spearow     = make_pokemon("021", "Spearow",        [normal, flying],(40, 60, 30, 70, "base_weak"))
fearow      = make_pokemon("022", "Fearow",         [normal, flying],(65, 90, 65, 100, "fast"))

ekans       = make_pokemon("023", "Ekans",          [poison],        (35, 60, 44, 55, "base_mid"))
arbok       = make_pokemon("024", "Arbok",          [poison],        (60, 95, 69, 80, "base_mid"))

pikachu     = make_pokemon("025", "Pikachu",        [electric],      (35, 55, 40, 90, "fast"))
raichu      = make_pokemon("026", "Raichu",         [electric],      (60, 90, 55, 110, "fast"))

sandshrew   = make_pokemon("027", "Sandshrew",      [ground],        (50, 75, 85, 40, "base_mid"))
sandslash   = make_pokemon("028", "Sandslash",      [ground],        (75, 100, 110, 65, "base_mid"))

nidoran_f   = make_pokemon("029", "Nidoran♀",       [poison],        (55, 47, 52, 41, "base_mid"))
nidorina    = make_pokemon("030", "Nidorina",       [poison],        (70, 62, 67, 56, "intermediate"))
nidoqueen   = make_pokemon("031", "Nidoqueen",      [poison, ground],(90, 92, 87, 76, "final"))

nidoran_m   = make_pokemon("032", "Nidoran♂",       [poison],        (46, 57, 40, 50, "base_mid"))
nidorino    = make_pokemon("033", "Nidorino",       [poison],        (61, 72, 57, 65, "intermediate"))
nidoking    = make_pokemon("034", "Nidoking",       [poison, ground],(81, 102, 77, 85, "final"))

clefairy    = make_pokemon("035", "Clefairy",       [fairy],         (70, 45, 48, 35, "base_mid"))
clefable    = make_pokemon("036", "Clefable",       [fairy],         (95, 70, 73, 60, "final"))

vulpix      = make_pokemon("037", "Vulpix",         [fire],          (38, 41, 40, 65, "base_mid"))
ninetales   = make_pokemon("038", "Ninetales",      [fire],          (73, 76, 75,100, "final"))

jigglypuff  = make_pokemon("039", "Jigglypuff",     [normal, fairy], (115, 45, 20, 20, "base_mid"))
wigglytuff  = make_pokemon("040", "Wigglytuff",     [normal, fairy], (140, 70, 45, 45, "final"))

zubat       = make_pokemon("041", "Zubat",          [poison, flying],(40, 45, 35, 55, "base_weak"))
golbat      = make_pokemon("042", "Golbat",         [poison, flying],(75, 80, 70, 90, "base_mid"))

oddish      = make_pokemon("043", "Oddish",         [grass, poison], (45, 50, 55, 30, "base_mid"))
gloom       = make_pokemon("044", "Gloom",          [grass, poison], (60, 65, 70, 40, "intermediate"))
vileplume   = make_pokemon("045", "Vileplume",      [grass, poison], (75, 80, 85, 50, "final"))

paras       = make_pokemon("046", "Paras",          [bug, grass],    (35, 70, 55, 25, "base_mid"))
parasect    = make_pokemon("047", "Parasect",       [bug, grass],    ("base_mid"))

venonat     = make_pokemon("048", "Venonat",        [bug, poison],   ("base_mid"))
venomoth    = make_pokemon("049", "Venomoth",       [bug, poison],   ("fast"))

diglett     = make_pokemon("050", "Diglett",        [ground],        ("fast"))
dugtrio     = make_pokemon("051", "Dugtrio",        [ground],        ("fast"))

meowth      = make_pokemon("052", "Meowth",         [normal],        ("base_mid"))
persian     = make_pokemon("053", "Persian",        [normal],        ("fast"))

psyduck     = make_pokemon("054", "Psyduck",        [water],         ("base_mid"))
golduck     = make_pokemon("055", "Golduck",        [water],         ("base_mid"))

mankey      = make_pokemon("056", "Mankey",         [fighting],      ("base_mid"))
primeape    = make_pokemon("057", "Primeape",       [fighting],      ("base_mid"))

growlithe   = make_pokemon("058", "Growlithe",      [fire],          ("base_mid"))
arcanine    = make_pokemon("059", "Arcanine",       [fire],          ("final"))

poliwag     = make_pokemon("060", "Poliwag",        [water],         ("base_mid"))
poliwhirl   = make_pokemon("061", "Poliwhirl",      [water],         ("intermediate"))
poliwrath   = make_pokemon("062", "Poliwrath",      [water, fighting],("final"))

abra        = make_pokemon("063", "Abra",           [psychic],       ())
kadabra     = make_pokemon("064", "Kadabra",        [psychic],       ("intermediate"))
alakazam    = make_pokemon("065", "Alakazam",       [psychic],       ("fast"))

machop      = make_pokemon("066", "Machop",         [fighting],      ("base_mid"))
machoke     = make_pokemon("067", "Machoke",        [fighting],      ("intermediate"))
machamp     = make_pokemon("068", "Machamp",        [fighting],      ("final"))

bellsprout  = make_pokemon("069", "Bellsprout",     [grass, poison], ("base_mid"))
weepinbell  = make_pokemon("070", "Weepinbell",     [grass, poison], ("intermediate"))
victreebel  = make_pokemon("071", "Victreebel",     [grass, poison], ("final"))

tentacool   = make_pokemon("072", "Tentacool",      [water, poison], ("base_mid"))
tentacruel  = make_pokemon("073", "Tentacruel",     [water, poison], ("base_mid"))

geodude     = make_pokemon("074", "Geodude",        [rock, ground],  ("tank"))
graveler    = make_pokemon("075", "Graveler",       [rock, ground],  ("tank"))
golem       = make_pokemon("076", "Golem",          [rock, ground],  ("tank"))

ponyta      = make_pokemon("077", "Ponyta",         [fire],          ("fast"))
rapidash    = make_pokemon("078", "Rapidash",       [fire],          ("fast"))

slowpoke    = make_pokemon("079", "Slowpoke",       [water, psychic],("base_mid"))
slowbro     = make_pokemon("080", "Slowbro",        [water, psychic],("tank"))

magnemite   = make_pokemon("081", "Magnemite",      [electric, steel],("base_mid"))
magneton    = make_pokemon("082", "Magneton",       [electric, steel],("base_mid"))

farfetchd   = make_pokemon("083", "Farfetch'd",     [normal, flying],("base_mid"))

doduo       = make_pokemon("084", "Doduo",          [normal, flying],("base_mid"))
dodrio      = make_pokemon("085", "Dodrio",         [normal, flying],("fast"))

seel        = make_pokemon("086", "Seel",           [water],         ("base_mid"))
dewgong     = make_pokemon("087", "Dewgong",        [water, ice],    ("base_mid"))

grimer      = make_pokemon("088", "Grimer",         [poison],        ("base_mid"))
muk         = make_pokemon("089", "Muk",            [poison],        ("tank"))

shellder    = make_pokemon("090", "Shellder",       [water],         ("base_mid"))
cloyster    = make_pokemon("091", "Cloyster",       [water, ice],    ("tank"))

gastly      = make_pokemon("092", "Gastly",         [ghost, poison], ("base_mid"))
haunter     = make_pokemon("093", "Haunter",        [ghost, poison], ("intermediate"))
gengar      = make_pokemon("094", "Gengar",         [ghost, poison], ("final"))

onix        = make_pokemon("095", "Onix",           [rock, ground],  ("tank"))

drowzee     = make_pokemon("096", "Drowzee",        [psychic],       ("base_mid"))
hypno       = make_pokemon("097", "Hypno",          [psychic],       ("base_mid"))

krabby      = make_pokemon("098", "Krabby",         [water],         ("base_mid"))
kingler     = make_pokemon("099", "Kingler",        [water],         ("base_mid"))

voltorb     = make_pokemon("100", "Voltorb",        [electric],      ("fast"))
electrode   = make_pokemon("101", "Electrode",      [electric],      ("fast"))

exeggcute   = make_pokemon("102", "Exeggcute",      [grass, psychic],("base_mid"))
exeggutor   = make_pokemon("103", "Exeggutor",      [grass, psychic],("final"))

cubone      = make_pokemon("104", "Cubone",         [ground],        ("base_mid"))
marowak     = make_pokemon("105", "Marowak",        [ground],        ("base_mid"))

hitmonlee   = make_pokemon("106", "Hitmonlee",      [fighting],      ("base_mid"))
hitmonchan  = make_pokemon("107", "Hitmonchan",     [fighting],      ("base_mid"))

lickitung   = make_pokemon("108", "Lickitung",      [normal],        ("base_mid"))

koffing     = make_pokemon("109", "Koffing",        [poison],        ("base_mid"))
weezing     = make_pokemon("110", "Weezing",        [poison],        ("tank"))

rhyhorn     = make_pokemon("111", "Rhyhorn",        [ground, rock],  ("tank"))
rhydon      = make_pokemon("112", "Rhydon",         [ground, rock],  ("tank"))

chansey     = make_pokemon("113", "Chansey",        [normal],        ("tank"))

tangela     = make_pokemon("114", "Tangela",        [grass],         ("base_mid"))

kangaskhan  = make_pokemon("115", "Kangaskhan",     [normal],        ("base_mid"))

horsea      = make_pokemon("116", "Horsea",         [water],         ("base_mid"))
seadra      = make_pokemon("117", "Seadra",         [water],         ("base_mid"))

goldeen     = make_pokemon("118", "Goldeen",        [water],         ("base_mid"))
seaking     = make_pokemon("119", "Seaking",        [water],         ("base_mid"))

staryu      = make_pokemon("120", "Staryu",         [water],         ("fast"))
starmie     = make_pokemon("121", "Starmie",        [water, psychic],("fast"))

mr_mime     = make_pokemon("122", "Mr. Mime",       [psychic, fairy],("base_mid"))

scyther     = make_pokemon("123", "Scyther",        [bug, flying],   ("fast"))

jynx        = make_pokemon("124", "Jynx",           [ice, psychic],  ("base_mid"))

electabuzz  = make_pokemon("125", "Electabuzz",     [electric],      ("base_mid"))
magmar      = make_pokemon("126", "Magmar",         [fire],          ("base_mid"))

pinsir      = make_pokemon("127", "Pinsir",         [bug],           ("base_mid"))

tauros      = make_pokemon("128", "Tauros",         [normal],        ("fast"))

magikarp    = make_pokemon("129", "Magikarp",       [water],         ())
gyarados    = make_pokemon("130", "Gyarados",       [water, flying], ("final"))

lapras      = make_pokemon("131", "Lapras",         [water, ice],    ("final"))

ditto       = make_pokemon("132", "Ditto",          [normal],        ("base_mid"))

eevee       = make_pokemon("133", "Eevee",          [normal],        ("base_mid"))
vaporeon    = make_pokemon("134", "Vaporeon",       [water],         ("final"))
jolteon     = make_pokemon("135", "Jolteon",        [electric],      ("fast"))
flareon     = make_pokemon("136", "Flareon",        [fire],          ("final"))

porygon     = make_pokemon("137", "Porygon",        [normal],        ("base_mid"))

omanyte     = make_pokemon("138", "Omanyte",        [rock, water],   ("base_mid"))
omastar     = make_pokemon("139", "Omastar",        [rock, water],   ("tank"))

kabuto      = make_pokemon("140", "Kabuto",         [rock, water],   ("base_mid"))
kabutops    = make_pokemon("141", "Kabutops",       [rock, water],   ("base_mid"))

aerodactyl  = make_pokemon("142", "Aerodactyl",     [rock, flying],  ("fast"))

snorlax     = make_pokemon("143", "Snorlax",        [normal],        ("tank"))

articuno    = make_pokemon("144", "Articuno",       [ice, flying],   "legend")
zapdos      = make_pokemon("145", "Zapdos",         [electric, flying],"legend")
moltres     = make_pokemon("146", "Moltres",        [fire, flying],  "legend")

dratini     = make_pokemon("147", "Dratini",        [dragon],        ("base_mid"))
dragonair   = make_pokemon("148", "Dragonair",      [dragon],        ("intermediate"))
dragonite   = make_pokemon("149", "Dragonite",      [dragon, flying],("final"))

mewtwo      = make_pokemon("150", "Mewtwo",         [psychic],       ("legend"))
mew         = make_pokemon("151", "Mew",            [psychic],       ("legend"))

# kanto_pokemons = [
#     bulbasaur, ivysaur, venusaur,charmander, charmeleon, charizard,squirtle, wartortle, blastoise,
#     caterpie, metapod, butterfree,weedle, kakuna, beedrill,pidgey, pidgeotto, pidgeot,rattata, raticate,
#     spearow, fearow,ekans, arbok,pikachu, raichu,sandshrew, sandslash,nidoran_f, nidorina, nidoqueen,
#     nidoran_m, nidorino, nidoking,clefairy, clefable,vulpix, ninetales,jigglypuff, wigglytuff,zubat, golbat,
#     oddish, gloom, vileplume,paras, parasect,venonat, venomoth,diglett, dugtrio,meowth, persian,
#     psyduck, golduck,mankey, primeape,growlithe, arcanine,poliwag, poliwhirl, poliwrath,abra, kadabra, alakazam,
#     machop, machoke, machamp,bellsprout, weepinbell, victreebel,tentacool, tentacruel,geodude, graveler, golem,
#     ponyta, rapidash,slowpoke, slowbro,magnemite, magneton,farfetchd,doduo, dodrio,seel, dewgong,grimer, muk,
#     shellder, cloyster,gastly, haunter, gengar,onix,drowzee, hypno,krabby, kingler,voltorb, electrode,
#     exeggcute, exeggutor,cubone, marowak,hitmonlee, hitmonchan,lickitung,koffing, weezing,rhyhorn, rhydon,chansey,
#     tangela,kangaskhan,horsea, seadra,goldeen, seaking,staryu, starmie,mr_mime,scyther,jynx,electabuzz,magmar,
#     pinsir, tauros, magikarp, gyarados, lapras, ditto, eevee, vaporeon, jolteon, flareon, porygon, omanyte, omastar, kabuto, 
#     kabutops, aerodactyl, snorlax, articuno, zapdos, moltres, dratini, dragonair, dragonite, mewtwo, mew]

kanto_pokemons = [bulbasaur, ivysaur, venusaur, squirtle, charmander, charmeleon]
