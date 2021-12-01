#!/usr/bin/env python
# coding: utf-8

# # Conditional expressions
# _flow control_ statements.
# `if`
# `elif`
# `else`

# Een `if` statement begint altijd met `if`.
# Kan meerdere `elif` bevatten.
# En eindigt met een `else` als dit nodig is.


# Een `if` statement maakt een splitsing in de code.
# De code komt in het `if` _code block_ als de expressie waar is.

num = 5

# alleen als num tussen 0 en 10 is ...
if 0 <= num < 10:
    add = 10 - num  # bereken hoeveel toe te voegen tot 10
    print(f'{num} + {add} = 10')
    num += add  # tel het nummer erbij op om 10 te krijgen

print(num)


# De code komt in een `else` _code block_ als de expressie(s) ervoor een `False` zijn.

num = 15

# alleen als num tussen 0 en 10 is ...
if 0 <= num < 10:
    add = 10 - num  # bereken hoeveel toe te voegen tot 10
    print(f'{num} + {add} = 10')
    num += add  # tel het nummer erbij op om 10 te krijgen
else:
    print(f'num is  groter dan 10: {num}')

print(num)


# Met een `if elif` statement kan er meerdere expressies
# De statements worden van `if`, `elif` naar `else` gevolgd.
# Dus als een `if` of `elif` expressie waar is worden andere `elif` statements niet meer gechecked.
# Weredom, als alles een `False` is komt de code in het `else` _code block_.

num = 25

# alleen als num tussen 0 en 10 is ...
if 0 <= num < 10:
    add = 10 - num  # bereken hoeveel toe te voegen tot 10
    print(f'{num} + {add} = 10')
    num += add  # tel het nummer erbij op om 10 te krijgen

# of alleen als num groter is dan 10 ...
elif num >= 10:
    sub = num - 10  # bereken hoeveel er af te halen
    print(f'{num} - {sub} = 10')
    num -= sub  # haal het nummer er af op 10 te krijgen

# num is negatief.
else:
    print(f'num is negatief: {num}')

print(num)


# ### Oefeningen Conditional expressions

# Maak een `if` `else` blok wat checkt of het `dag` variable een dag bevat dat in het weekend valt.
# Zodra de `dag` in het weekend valt zet de `is_weekend` variable op `True`, zo niet dan `False`.

# Vul hieronder de code aan.

is_weekend = None  # bool
dag = "maandag"  # verander dit naar een andere dag

# Verwijder dit blok commentaar
#   en maak hier logica dat bepaald of de `dag` in het weekend valt.

if ... :
    ...
else:
    ...

print(is_weekend)
