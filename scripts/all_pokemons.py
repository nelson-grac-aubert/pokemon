from pokemon_class import Pokemon
from types import normal, fire, water, grass, electric, ice, fighting, poison, ground, flying, psychic, bug, rock, ghost, dragon, dark, steel, fairy

# ---------------------------------------------------------------------------
# Helper: stats per role
# ---------------------------------------------------------------------------

ROLE_STATS = {
    "base_weak":   (45, 45, 45, 45, 85),
    "base_mid":    (55, 55, 55, 55, 90),
    "intermediate":(65, 65, 65, 60, 92),
    "final":       (80, 80, 80, 75, 95),
    "fast":        (55, 50, 45, 90, 98),
    "tank":        (70, 60, 90, 40, 88),
    "legend":      (100, 100, 100, 100, 100),
}

def make_pokemon(pid: str, name: str, types_list: list, role: str) -> Pokemon:
    hp, atk, df, spd, prec = ROLE_STATS[role]
    return Pokemon(
        name=name,
        hp=hp,
        attack=atk,
        defense=df,
        speed=spd,
        precision=prec,
        types=types_list,
        id=pid
    )

# ---------------------------------------------------------------------------
# Kanto Pokédex (001–151)
# ---------------------------------------------------------------------------

bulbasaur   = make_pokemon("001", "Bulbizarre",      [grass, poison], "base_mid")
ivysaur     = make_pokemon("002", "Herbizarre",      [grass, poison], "intermediate")
venusaur    = make_pokemon("003", "Florizarre",      [grass, poison], "final")

charmander  = make_pokemon("004", "Salamèche",       [fire],          "base_mid")
charmeleon  = make_pokemon("005", "Reptincel",       [fire],          "intermediate")
charizard   = make_pokemon("006", "Dracaufeu",       [fire, flying],  "final")

squirtle    = make_pokemon("007", "Carapuce",        [water],         "base_mid")
wartortle   = make_pokemon("008", "Carabaffe",       [water],         "intermediate")
blastoise   = make_pokemon("009", "Tortank",         [water],         "final")

caterpie    = make_pokemon("010", "Chenipan",        [bug],           "base_weak")
metapod     = make_pokemon("011", "Chrysacier",      [bug],           "base_weak")
butterfree  = make_pokemon("012", "Papilusion",      [bug, flying],   "fast")

weedle      = make_pokemon("013", "Aspicot",         [bug, poison],   "base_weak")
kakuna      = make_pokemon("014", "Coconfort",       [bug, poison],   "base_weak")
beedrill    = make_pokemon("015", "Dardargnan",      [bug, poison],   "fast")

pidgey      = make_pokemon("016", "Roucool",         [normal, flying],"base_weak")
pidgeotto   = make_pokemon("017", "Roucoups",        [normal, flying],"intermediate")
pidgeot     = make_pokemon("018", "Roucarnage",      [normal, flying],"fast")

rattata     = make_pokemon("019", "Rattata",         [normal],        "base_weak")
raticate    = make_pokemon("020", "Rattatac",        [normal],        "base_mid")

spearow     = make_pokemon("021", "Piafabec",        [normal, flying],"base_weak")
fearow      = make_pokemon("022", "Rapasdepic",      [normal, flying],"fast")

ekans       = make_pokemon("023", "Abo",             [poison],        "base_mid")
arbok       = make_pokemon("024", "Arbok",           [poison],        "base_mid")

pikachu     = make_pokemon("025", "Pikachu",         [electric],      "fast")
raichu      = make_pokemon("026", "Raichu",          [electric],      "fast")

sandshrew   = make_pokemon("027", "Sabelette",       [ground],        "base_mid")
sandslash   = make_pokemon("028", "Sablaireau",      [ground],        "base_mid")

nidoran_f   = make_pokemon("029", "Nidoran♀",        [poison],        "base_mid")
nidorina    = make_pokemon("030", "Nidorina",        [poison],        "intermediate")
nidoqueen   = make_pokemon("031", "Nidoqueen",       [poison, ground],"final")

nidoran_m   = make_pokemon("032", "Nidoran♂",        [poison],        "base_mid")
nidorino    = make_pokemon("033", "Nidorino",        [poison],        "intermediate")
nidoking    = make_pokemon("034", "Nidoking",        [poison, ground],"final")

clefairy    = make_pokemon("035", "Mélofée",         [fairy],         "base_mid")
clefable    = make_pokemon("036", "Mélodelfe",       [fairy],         "final")

vulpix      = make_pokemon("037", "Goupix",          [fire],          "base_mid")
ninetales   = make_pokemon("038", "Feunard",         [fire],          "final")

jigglypuff  = make_pokemon("039", "Rondoudou",       [normal, fairy], "base_mid")
wigglytuff  = make_pokemon("040", "Grodoudou",       [normal, fairy], "final")

zubat       = make_pokemon("041", "Nosferapti",      [poison, flying],"base_weak")
golbat      = make_pokemon("042", "Nosferalto",      [poison, flying],"base_mid")

oddish      = make_pokemon("043", "Mystherbe",       [grass, poison], "base_mid")
gloom       = make_pokemon("044", "Ortide",          [grass, poison], "intermediate")
vileplume   = make_pokemon("045", "Rafflesia",       [grass, poison], "final")

paras       = make_pokemon("046", "Paras",           [bug, grass],    "base_mid")
parasect    = make_pokemon("047", "Parasect",        [bug, grass],    "base_mid")

venonat     = make_pokemon("048", "Mimitoss",        [bug, poison],   "base_mid")
venomoth    = make_pokemon("049", "Aéromite",        [bug, poison],   "fast")

diglett     = make_pokemon("050", "Taupiqueur",      [ground],        "fast")
dugtrio     = make_pokemon("051", "Triopikeur",      [ground],        "fast")

meowth      = make_pokemon("052", "Miaouss",         [normal],        "base_mid")
persian     = make_pokemon("053", "Persian",         [normal],        "fast")

psyduck     = make_pokemon("054", "Psykokwak",       [water],         "base_mid")
golduck     = make_pokemon("055", "Akwakwak",        [water],         "base_mid")

mankey      = make_pokemon("056", "Férosinge",       [fighting],      "base_mid")
primeape    = make_pokemon("057", "Colossinge",      [fighting],      "base_mid")

growlithe   = make_pokemon("058", "Caninos",         [fire],          "base_mid")
arcanine    = make_pokemon("059", "Arcanin",         [fire],          "final")

poliwag     = make_pokemon("060", "Ptitard",         [water],         "base_mid")
poliwhirl   = make_pokemon("061", "Têtarte",         [water],         "intermediate")
poliwrath   = make_pokemon("062", "Tartard",         [water, fighting],"final")

abra        = make_pokemon("063", "Abra",            [psychic],       "base_weak")
kadabra     = make_pokemon("064", "Kadabra",         [psychic],       "intermediate")
alakazam    = make_pokemon("065", "Alakazam",        [psychic],       "fast")

machop      = make_pokemon("066", "Machoc",          [fighting],      "base_mid")
machoke     = make_pokemon("067", "Machopeur",       [fighting],      "intermediate")
machamp     = make_pokemon("068", "Mackogneur",      [fighting],      "final")

bellsprout  = make_pokemon("069", "Chétiflor",       [grass, poison], "base_mid")
weepinbell  = make_pokemon("070", "Boustiflor",      [grass, poison], "intermediate")
victreebel  = make_pokemon("071", "Empiflor",        [grass, poison], "final")

tentacool   = make_pokemon("072", "Tentacool",       [water, poison], "base_mid")
tentacruel  = make_pokemon("073", "Tentacruel",      [water, poison], "base_mid")

geodude     = make_pokemon("074", "Racaillou",       [rock, ground],  "tank")
graveler    = make_pokemon("075", "Gravalanch",      [rock, ground],  "tank")
golem       = make_pokemon("076", "Grolem",          [rock, ground],  "tank")

ponyta      = make_pokemon("077", "Ponyta",          [fire],          "fast")
rapidash    = make_pokemon("078", "Galopa",          [fire],          "fast")

slowpoke    = make_pokemon("079", "Ramoloss",        [water, psychic],"base_mid")
slowbro     = make_pokemon("080", "Flagadoss",       [water, psychic],"tank")

magnemite   = make_pokemon("081", "Magnéti",         [electric, steel],"base_mid")
magneton    = make_pokemon("082", "Magnéton",        [electric, steel],"base_mid")

farfetchd   = make_pokemon("083", "Canarticho",      [normal, flying],"base_mid")

doduo       = make_pokemon("084", "Doduo",           [normal, flying],"base_mid")
dodrio      = make_pokemon("085", "Dodrio",          [normal, flying],"fast")

seel        = make_pokemon("086", "Otaria",          [water],         "base_mid")
dewgong     = make_pokemon("087", "Lamantine",       [water, ice],    "base_mid")

grimer      = make_pokemon("088", "Tadmorv",         [poison],        "base_mid")
muk         = make_pokemon("089", "Grotadmorv",      [poison],        "tank")

shellder    = make_pokemon("090", "Kokiyas",         [water],         "base_mid")
cloyster    = make_pokemon("091", "Crustabri",       [water, ice],    "tank")

gastly      = make_pokemon("092", "Fantominus",      [ghost, poison], "base_mid")
haunter     = make_pokemon("093", "Spectrum",        [ghost, poison], "intermediate")
gengar      = make_pokemon("094", "Ectoplasma",      [ghost, poison], "final")

onix        = make_pokemon("095", "Onix",            [rock, ground],  "tank")

drowzee     = make_pokemon("096", "Soporifik",       [psychic],       "base_mid")
hypno       = make_pokemon("097", "Hypnomade",       [psychic],       "base_mid")

krabby      = make_pokemon("098", "Krabby",          [water],         "base_mid")
kingler     = make_pokemon("099", "Krabboss",        [water],         "base_mid")

voltorb     = make_pokemon("100", "Voltorbe",        [electric],      "fast")
electrode   = make_pokemon("101", "Électrode",       [electric],      "fast")

exeggcute   = make_pokemon("102", "Noeunoeuf",       [grass, psychic],"base_mid")
exeggutor   = make_pokemon("103", "Noadkoko",        [grass, psychic],"final")

cubone      = make_pokemon("104", "Osselait",        [ground],        "base_mid")
marowak     = make_pokemon("105", "Ossatueur",       [ground],        "base_mid")

hitmonlee   = make_pokemon("106", "Kicklee",         [fighting],      "base_mid")
hitmonchan  = make_pokemon("107", "Tygnon",          [fighting],      "base_mid")

lickitung   = make_pokemon("108", "Excelangue",      [normal],        "base_mid")

koffing     = make_pokemon("109", "Smogo",           [poison],        "base_mid")
weezing     = make_pokemon("110", "Smogogo",         [poison],        "tank")

rhyhorn     = make_pokemon("111", "Rhinocorne",      [ground, rock],  "tank")
rhydon      = make_pokemon("112", "Rhinoféros",      [ground, rock],  "tank")

chansey     = make_pokemon("113", "Leveinard",       [normal],        "tank")

tangela     = make_pokemon("114", "Saquedeneu",      [grass],         "base_mid")

kangaskhan  = make_pokemon("115", "Kangourex",       [normal],        "base_mid")

horsea      = make_pokemon("116", "Hypotrempe",      [water],         "base_mid")
seadra      = make_pokemon("117", "Hypocéan",        [water],         "base_mid")

goldeen     = make_pokemon("118", "Poissirène",      [water],         "base_mid")
seaking     = make_pokemon("119", "Poissoroy",       [water],         "base_mid")

staryu      = make_pokemon("120", "Stari",           [water],         "fast")
starmie     = make_pokemon("121", "Staross",         [water, psychic],"fast")

mr_mime     = make_pokemon("122", "M. Mime",         [psychic, fairy],"base_mid")

scyther     = make_pokemon("123", "Insécateur",      [bug, flying],   "fast")

jynx        = make_pokemon("124", "Lippoutou",       [ice, psychic],  "base_mid")

electabuzz  = make_pokemon("125", "Élektek",         [electric],      "base_mid")
magmar      = make_pokemon("126", "Magmar",          [fire],          "base_mid")

pinsir      = make_pokemon("127", "Scarabrute",      [bug],           "base_mid")

tauros      = make_pokemon("128", "Tauros",          [normal],        "fast")

magikarp    = make_pokemon("129", "Magicarpe",       [water],         "base_weak")
gyarados    = make_pokemon("130", "Léviator",        [water, flying], "final")

lapras      = make_pokemon("131", "Lokhlass",        [water, ice],    "final")

ditto       = make_pokemon("132", "Métamorph",       [normal],        "base_mid")

eevee       = make_pokemon("133", "Évoli",           [normal],        "base_mid")
vaporeon    = make_pokemon("134", "Aquali",          [water],         "final")
jolteon     = make_pokemon("135", "Voltali",         [electric],      "fast")
flareon     = make_pokemon("136", "Pyroli",          [fire],          "final")

porygon     = make_pokemon("137", "Porygon",         [normal],        "base_mid")

omanyte     = make_pokemon("138", "Amonita",         [rock, water],   "base_mid")
omastar     = make_pokemon("139", "Amonistar",       [rock, water],   "tank")

kabuto      = make_pokemon("140", "Kabuto",          [rock, water],   "base_mid")
kabutops    = make_pokemon("141", "Kabutops",        [rock, water],   "base_mid")

aerodactyl  = make_pokemon("142", "Ptéra",           [rock, flying],  "fast")

snorlax     = make_pokemon("143", "Ronflex",         [normal],        "tank")

articuno    = make_pokemon("144", "Artikodin",       [ice, flying],   "legend")
zapdos      = make_pokemon("145", "Électhor",        [electric, flying],"legend")
moltres     = make_pokemon("146", "Sulfura",         [fire, flying],  "legend")

dratini     = make_pokemon("147", "Minidraco",       [dragon],        "base_mid")
dragonair   = make_pokemon("148", "Draco",           [dragon],        "intermediate")
dragonite   = make_pokemon("149", "Dracolosse",      [dragon, flying],"final")

mewtwo      = make_pokemon("150", "Mewtwo",          [psychic],       "legend")
mew         = make_pokemon("151", "Mew",             [psychic],       "legend")

KANTO_POKEMON = [
    bulbasaur, ivysaur, venusaur, charmander, charmeleon, charizard, squirtle, wartortle, blastoise,
    caterpie, metapod, butterfree, weedle, kakuna, beedrill, pidgey, pidgeotto, pidgeot, rattata, raticate,
    spearow, fearow, ekans, arbok, pikachu, raichu, sandshrew, sandslash,nidoran_f, nidorina, nidoqueen,
    nidoran_m, nidorino, nidoking,clefairy, clefable,vulpix, ninetales,jigglypuff, wigglytuff,zubat, golbat,
    oddish, gloom, vileplume,paras, parasect,venonat, venomoth,diglett, dugtrio,meowth, persian,psyduck, golduck,
    mankey, primeape,growlithe, arcanine,poliwag, poliwhirl, poliwrath,abra, kadabra, alakazam,machop, machoke, 
    machamp,bellsprout, weepinbell, victreebel,tentacool, tentacruel,geodude, graveler, golem,ponyta, rapidash,
    slowpoke, slowbro,magnemite, magneton,farfetchd,doduo, dodrio,seel, dewgong,grimer, muk,shellder, cloyster,
    gastly, haunter, gengar,onix,drowzee, hypno,krabby, kingler,voltorb, electrode,exeggcute, exeggutor,cubone, marowak,
    hitmonlee, hitmonchan,lickitung,koffing, weezing,rhyhorn, rhydon,chansey,tangela,kangaskhan,horsea, seadra,
    goldeen, seaking,staryu, starmie,mr_mime,scyther,jynx,electabuzz, magmar,pinsir,tauros,magikarp, gyarados,
    lapras,ditto,eevee, vaporeon, jolteon, flareon,porygon,omanyte, omastar,kabuto, kabutops,aerodactyl,
    snorlax,articuno, zapdos, moltres,dratini, dragonair, dragonite,mewtwo, mew
]