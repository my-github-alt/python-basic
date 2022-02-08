#!/usr/bin/env python
# coding: utf-8

# # Loops

# ## for-loop
# Met een for-loop kan je over een object itereren.  
# 
# De for-loops in Python zijn anders geschreven dan in andere programeertalen.  
# In veel talen wordt de for-loop zo geschreven:  
# ```
# for (int i = 0; i < 10; i++) {
#     ...
# };
# ```
# In Python is zo'n for-loop als hierboven niet te creëren.  
# De for-loops in Python lopen over de serie aan elementen in de gegeven data container.  
# 
# Hieronder een voorbeeld van een inefficiënte Python for-loop.  
# Deze loop print de letters in de `a_to_f` lijst door.  
# Variabele `i`, dat aangemaakt wordt door `range`, vraagt het element op de positie van de lijst op.  

a_to_f = ['A', 'B', 'C', 'D', 'E', 'F']

# vraag de lengte van a_to_f en maak een range van nummers
for i in range(0, len(a_to_f)):
    # vraag per loop de character op de index van `i`
    character = a_to_f[i]
    print(f'not Pythonic loop: {character}')


# De Python for-loops kunnen de objecten in de `list` direct opvragen.  
# Zoals hieronder is voorgebeeld.

a_to_f = ['A', 'B', 'C', 'D', 'E', 'F']

# deze for-loop is leesbaar en een stuk efficiënter
for character in a_to_f:
    print(f'Pythonic loop: {character}')


# ## [while-loop](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)
# De while-loop _loopt_ door totdat de gegeven expressie `False` wordt.  
# Als het nodig is om een `while` als loop te gebruiken, zorg er dan voor dat de loop niet oneindig is.  

# ```
# # voorbeeld dan een loop die nooit eindigt
# 
# while True:
#     print('Deze while-loop eindigt nooit!')
# ```

count = 10
while count > 0:  # loop zo lang de count groter is dan 0
    print(count, end=' ')
    count = count - 1


# ## continue
# `continue` is een statement dat gebruikt kan worden in een loop.  
# Zodra de loop een `continue` statement tegenkomt gaat de loop naar de volgende iteratie.  
# De code na de `continue` wordt dan niet uitgevoerd.  

# sla nummer 2 en 4 over met `continue`
for nummer in range(10):
    if nummer in {2, 4}:
        continue
        print("Dit wordt nooit uitgeprint.")
    else:
        print(nummer, end=' ')


# ## break
# Zodra de loop een `break` statement tegenkomt wordt de loop gestopt.  
# De code na de `break` wordt dan niet uitgevoerd.

# `break` de while loop als de count 10 is.
count = 0
while True:  # loop voor altijd
    if count >= 10:
        break
        print("Dit wordt nooit uitgeprint.")
    else:
        print(count, end=' ')
        count = count + 1

print('\nNa de loop')


# ### Itereer functies 
# Hieronder een paar hulpzame functies die veel gebruikt worden in for-loops.  

# ### zip
# `zip` is een built-in functie.  
# Deze functie rijgt de elementen in meerdere series aan elkaar als een soort ritssluiting.  

lijst_a = ['x', 'y', 'z']
tuple_b = ('a', 'b', 'c', 'd')
zipped = zip(lijst_a, tuple_b)   # `zip` twee series
print(f'{zipped = }')            # `zip` is, net als `range`, een luie functie
print(list(zipped))

# `zip` wordt net so lang als de kortste serie.  
# `zip` neemt alles aan zolang het object in combinatie met een loop gebruikt kan worden.

for a, x, y, z in zip("abc", [9, 8, 7], {1, 2, 3, 4}, (2, 3, 4)):   # `zip` 4 series
    som = x + y * z
    print(f'{a}: {x} + ({y} * {z}) = {som}')


# ### enumerate
# `enumerate` is een built-in functie dat de elementen in een serie een nummer geeft.

lijst = ['x', 'y', 'z']
enumerated = enumerate(lijst)   # `enumerate` de serie
print(f'{enumerated = }')       # `enumerate` is, net als `range`, een luie functie
print(list(enumerated))

for num, letter in enumerate(['l', 'o', 'o', 'p'], start=-1):   # specificeer vanaf waar te tellen met `start`
    print(f'{num}:\t{letter}')


# ### Oefeningen Loops
# 
# Opdracht 1:  
# Loop met een for-loop over het alphabet en break de loop zodra de letter `'m'` voorbij komt.  


# Opdracht 2:  
# Maak een alphabet van `'a'` tot `'z'` en maak een loop dat de waardes van `'z'` naar `'a'` uitprint.    


# Opdracht 3:
# Wat is de waarde van `nummer` na deze for-loop?
# 
# ```
# nummer = 11
# for nummer in range(10):
#     if nummer < 5:
#         continue
#         
# # wat is nummer nu?
# ```

