#!/usr/bin/env python
# coding: utf-8

# # Structural Pattern Matching
# 
# Veel programeertalen hebben en switch statement.  
# Sinds versie 3.10 heeft Python ook een _switch statement_ met de naam: Structural Pattern Matching.  
# Een grote naam voor iets wat simpel klinkt, maar het kan meer dan een gewone switch-statement.  
# De switch-case statement maakt gebruik van patroon vergelijking.  


# match-case statements zijn in python 3.10 geïntroduceerd.
# test voor de juiste Python versie.
import sys
major, minor, *_ = sys.version_info
assert major == 3 and minor <= 10, f"Python version 3.10 needed, used: {major}.{minor}"
# error? installeer de laatste Python versie
#   https://www.python.org/downloads/


# #### match-case statement
# Hieronder een match-case als klasieke switch-case statement

fruit = 'Banaan'

match fruit.lower():  # maak alle letters lower-case
    case 'appel':
        kleur = 'Rood'
    case 'peer':
        kleur = 'Groen'
    case 'banaan':./
         kleur = 'Geel'
    case _:  # else
        kleur = 'niet bekend'
        
print(f'De kleur van {fruit} is {kleur}.')


# ### De `_` in een match-case statement
# Een `_` (underscore) representeerd een 'wildcard' in de match-case statement.  
# Dit matched met alles maar mag niet gebruikt worden als de eerste case.  
# Het wordt veel gebruikt als _catch-all_ placeholder.  

# (X, Y)
coordinaat = (0, 1)

match coordinaat:
    case (x, y) if x == y:
        print('x en y is hetzeflde getal')
    case (0, _):
        print(f'X is precies 0')
    case (_, 0):
        print(f'Y is precies 0')
    case (_, _, _):
        print(f'coordinaat heeft 3 dimensies')
    case _:
        print('dit is geen valide coordinaat')


# ### De `|` in een match-case statement
# Een `|` (pipe) representeerd een [or] patroon.  
# In Python is er ook een `or` operator.  
# De `|` wordt op meerdere plekken in Python gebruikt als union.  
# de `or` operator wordt alleen gebruikt in logische expressies zoals in een `if` statement.  


http_400_code = 402

match http_400_code:
    case 400:
        response = 'Bad request'
    case 401 | 402 | 403:
        response = 'Authentication error'
    case 404:
        response = 'Not found'
    case 418:
        response = "I'm a teapot"
    case _:
        response = 'Other error'

print(f'code: {http_400_code} response: {response}')


# ### Het matchen van een patroon
# Zoals voorheen genoemd, de match-case statement kan meer dan een switch statement.  
# Het is vooral heel sterk in het matchen van patronen.  
# Ook is het mogenlijk om variabelen in het statement te _binden_.  
# Het 'binden' van variabelen kan gezien worden als impliciete variable assignment, dit gebeurd normaal met een `=`  
# 
# Hieronder een voorbeeld van een match-case statement met die variablen bind.  
# Het voorbeeld is een JSON wat uit een API van een webwinkel is te verwachten.  
# Het doel is om met de gegevens een persoonlijk profiel op te stellen.  


webwinkel_json = {'data': {'kledingstuk': 'broek', 'maat': 's', 'kleur': 'groen'}}
# webwinkel_json = {'data': {'kledingstuk': 'tshirt', 'maat': 'l', 'kleur': 'geel'}}
# webwinkel_json = {'data': {}}

match webwinkel_json['data']:
    case data if len(data) == 0:
        print('geen data gekregen')
    
    case {'kledingstuk': kledingstuk, 'maat': ('s' | 'm') as maat, 'kleur': kleur}:
        if maat == 's':
            classificatie = 'klein' 
        else:
            classificatie = 'middel-groot'
        print(f'Deze persoon is {classificatie}, heeft een {kledingstuk} met de kleur: {kleur}')
        
    case {'kledingstuk': kledingstuk, 'maat': 'l'}:
        print(f'Iemand met een groot postuur heeft een {kledingstuk} aangeschaft')
        

# ### Het matchen van types
# Het is ook mogenlijk om op een `type` of classificatie van een variabele te matchen.  
# Dit gebeurd met de `()` achter een type zoals: `int`.  
# De haakjes zijn nodig, dit geeft aan dat het een match moet zijn op basis van `type` of `class`.  
# Anders zal de data gebonden worden aan het opgegeven variabele.  

data: str = "string"
# data: int = 1_000_000
# data: float = 0.00001


match data:
    case int():
        print(f'{data} is een int')
    case float():
        print(f'{data:.6f} is een float')
    case str():
        print(f'{data} is een str')


# ---
# ### Switch-case alternatieven gebruikt in vorige Python versies.
# Het is goed om te weten dat er verschillen zijn in Python versies.  
# Soms kan het niet anders en moet er gewerkt worden met een oudere versie van Python.  
# Dan zijn er altijd alternatieve constructies te maken. Toch zijn deze niet zo flexibel als de match-case statements.

# #### Lookup table
# Hiervoor wordt er gebruikt gemaakt van een `dict`.

fruit = 'Appel'

kleur = {
    'appel': 'Rood',
    'peer': 'Groen',
    'banaan': 'Geel',
}.get(fruit.lower(), 'niet bekend')  # `dict` heeft een `get` functie die een default waarde kan teruggeven

print(f'De kleur van {fruit} is {kleur}.')


# #### if-elif-else condities
# Het gebruik van de equals-operators in de if-elif statements laat zien dat het netter is om een match-case statement er voor deze logica te gebruiken.

fruit = 'Peer'

fruit_l = fruit.lower()  # alleen lower-case letters
if fruit_l == 'appel':
    kleur = 'Rood'
elif fruit_l == 'peer':
    kleur = 'Groen'
elif fruit_l == 'banaan':
    kleur = 'Geel'
else:
    kleur = 'niet bekend'
    
print(f'De kleur van {fruit} is {kleur}.')


# ---
# ### Oefeningen Structural Patern Matching
# 
# Een API geeft aan welke dag van de week het is.  
# De API geeft een dictionary waarvan een key in de `dict` een weekdag aanduidt.  
# De API is niet consistent, de weekdag kan de volledige naam of een cijfer zijn.  
# 
# De opdracht voor deze oefening:
# > Filter de API output met `match` en `case` zodat er wordt uitgeprint of het weekend is of niet.
# 
# Gegeven is de `api` functie en de `WEEK` variabele.

import random

# Constant WEEK is een `tupel` van de dagen in de week. De week start op zondag.
# index  0         1          2          3           4            5          6
WEEK = ('zondag', 'maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag')

def api() -> dict[str, str | int]:
    """api dat een dict teruggeeft
    structuur van de dict: { data: { weekdag: (`str` of `int`) } }
    """
    dag: str = random.choice(WEEK)
    idx: int = WEEK.index(dag)
    return {'data': {'weekdag': random.choice((dag, idx))}}


# roep de api om de data te krijgen
data = api()

# voorbeeld
match data:
    # case ...:
    #     print("het is weekend")
    # case ...:
    #     print("het is doordeweeks")
    # case ...:
    # ...
    case _:
        print("onbekende dag")
