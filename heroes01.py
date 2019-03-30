from algorithms.max import max_generic
from algorithms.min import min_generic
from algorithms.sort import bubble_generic

heroes = [
    {
        'name': 'Tony Stark',
        'alias': 'Iron Man',
        'skill': 'Gazdag and Okos',
        'level': 7,
        'kinezet': 9,
        'humorerzek': 10
    },
    {
        'name': 'Steve Rogers',
        'alias': 'Captain America',
        'skill': 'Szóó Páverful',
        'level': 6,
        'kinezet': 8,
        'humorerzek': 5     
    },
    {
        'name': 'Scarlet Witch',
        'alias': 'Wanda Maximoff',
        'skill': 'Mindstone',
        'level': 8,
        'kinezet': 7,
        'humorerzek': 4
    },
    {
        'name': 'Black Widow',
        'alias': 'Natasha Alianovna Romanoff',
        'skill': 'Csinos és gyilkos',
        'level': 5,
        'kinezet': 6,
        'humorerzek': 5
    },
    {
        'name': 'Thor',
        'alias': 'Thor',
        'skill': 'God',
        'level': 9,
        'kinezet': 10,
        'humorerzek': 9
    },
]

# 0 -> Ha h1 és h2 egyenlőek
# 1 -> Ha h1 nagyobb
# -1 -> Ha h2 nagyobb


def szint_alapjan(h1, h2):
    if h1['level'] > h2['level']:
        return 1
    elif h1['level'] < h2['level']:
        return -1
    else:
        return 0


# 0 -> Ha h1 és h2 egyenlőek
# 1 -> Ha h1 nagyobb
# -1 -> Ha h2 nagyobb


def kinezet_alapjan(h1, h2):
    if h1['kinezet'] < h2['kinezet']:
        return -1
    elif h1['kinezet'] > h2['kinezet']:
        return 1
    else:
        return 0

def humorerzek_alapjan(h1, h2):
    if h1['humorerzek'] < h2['humorerzek']:
        return -1
    elif h1['humorerzek'] > h2['humorerzek']:
        return 1
    else:
        return 0

def get_max_level_hero():
    hero = max_generic(heroes, szint_alapjan)
    return hero


def get_sexiest_hero():
    hero = max_generic(heroes, kinezet_alapjan)
    return hero

def get_min_level_hero():
    hero = min_generic(heroes, szint_alapjan)
    return hero


def get_ugliest_hero():
    hero = min_generic(heroes, kinezet_alapjan)
    return hero

def get_funniest_hero():
    hero = max_generic(heroes, humorerzek_alapjan)
    return hero


def get_bubble_generic():
    adatok = heroes
    return bubble_generic (adatok, kinezet_alapjan)


#def get_bubble_generic():
 #   adatok=heroes
  #  return bubble_generic(adatok, humorerzek_alapjan)



def fight(h1, h2):
    if szint_alapjan(h1, h2) == 1:
        return h1
    elif szint_alapjan(h1, h2) == -1:
        return h2
    else:
        return None

def fight(h1, h2):
    if humorerzek_alapjan(h1, h2) == 1:
        return h1
    elif humorerzek_alapjan(h1, h2) == -1:
        return h2
    else:
        return None

for hero in heroes:
    for kulcs in hero:
        print(kulcs, "=", hero[kulcs])
    print('')



#print('Legerősebb', get_max_level_hero()['name'])
#print('Legszexibb', get_sexiest_hero()['name'])
#print('Legcsúnyább', get_ugliest_hero()['name'])
#print('Leggyengébb', get_min_level_hero()['name'])
#print('Legviccesebb', get_funniest_hero()['name'])
print('Legjobbak', get_bubble_generic())
#print('viccesek', get_bubble_generic())
#print('viccesek', sep = \n)



weakest = get_min_level_hero()
ugliest = get_ugliest_hero()
winner = fight(weakest, ugliest)

funniest = get_funniest_hero()
winner = fight(funniest, funniest)


#print('harc', weakest['name'], 'és', ugliest['name'], 'között')
if winner is not None:
    print('Győztes', winner['name'])
else:
     print('Döntetlen')

#print('harc', funniest['name'], 'és', funniest['name'], 'között')
if winner is not None:
    print('Győztes', winner['name'])
else:
    print('Döntetlen')