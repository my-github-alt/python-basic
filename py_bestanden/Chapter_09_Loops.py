#!/usr/bin/env python
# coding: utf-8

# # Loops

# ## for-loop
# Met een for-loop kan je over een object itereren.

# De for-loops in Python zijn anders geschreven dan in andere de meeste andere programeertalen.
# Hieronder een Python for-loop dat over een `list` itereert door de index van de `list` te verhogen.

a_to_f = ['A', 'B', 'C', 'D', 'E', 'F']

# vraag de lengte van a_to_f en maak een range van nummers
for i in range(0, len(a_to_f)):
    # vraag per loop de character op de index van `i`
    character = a_to_f[i]
    print(f'not Pythonic loop: {character}')


# Python for-loops kunnen de objecten in de `list` direct opvragen.
# Zoals hieronder is voorgebeeld.

a_to_f = ['A', 'B', 'C', 'D', 'E', 'F']

# deze for-loop is leesbaar en een stuk efficiënter
for character in a_to_f:
    print(f'Pythonic loop: {character}')


# ## while-loop
# De while-loop loopt door totdat de gegeven expressie `False` wordt.

# voorbeeld dan een loop die nooit eindigt

"""
while True:
    print('Deze while-loop eindigt nooit!')
"""

count = 10
while count != 0:  # loop zo lang de count niet gelijk is aan 0
    print(count, end=' ')
    count = count - 1


# ## continue
# `continue` is een statement die gebruikt kan worden in een loop.
# Zodra de loop een `continue` statement tegenkomt gaat de loop naar de volgende iteratie.


# sla nummer 2 en 4 over met `continue`
for nummer in range(10):
    if nummer in {2, 4}:
        continue
    else:
        print(nummer, end=' ')


# ## break
# `break` de while loop als de count 10 is.
count = 0
while True:  # loop voor altijd
    if count >= 10:
        break
    else:
        print(count, end=' ')
        count = count + 1


# ### Oefeningen Loops

# Opdracht 1:
# Loop met een for-loop over het alphabet en break de loop zodra de letter `'m'` voorbij komt.



# Opdracht 2:
# Maak een alphabet van `'a'` tot `'z'` en maak een loop dat de waardes van `'z'` naar `'a'` uitprint.



# Opdracht 3:
# Wat is de waarde van `nummer` na deze for-loop?

"""
nummer = 11
for nummer in range(10):
    if nummer < 5:
        continue
"""
# wat is nummer nu?

