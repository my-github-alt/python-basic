#!/usr/bin/env python
# coding: utf-8

# # Exception handling

# `try`
# `except`
# `finally`

# Mensen maken fouten en programmas worden door mensen geschreven.

# Fouten in een programma kan je opvangen met `try` `except`.
# In de `try` statement zet je een stuk code dat fout kan gaan.
# Het blokje code onder de `except` statement vangt de fout op.

# Normaal stopt het programma bij een error, maar als de error is opgevangen gaat het door.

# ## try except

try:
    # `raise` express een AssertionError
    fout_waarde = 10 < 0
    assert fout_waarde, 'er is iets fout gegaan'
except Exception as err_msg:
    print(f'error: {err_msg}')

print('na de try-except')


# ### Multiple excepts

for num in (3, 2, 1, 0):
    try:
        # een 
        uitkomst = 10 / num
        print(f'10 gedeeld door {num} is: {uitkomst}')
    except ZeroDivisionError:
        print(f'10 kan niet gedeld worden door 0')
    except Exception as err_msg:
        print(f'log: Er is een onbekende fout opgetreden: {err_msg}')
        print('stop het programma')
        exit(1)


# ## finally

print('open een nieuw bestand')
# mode van open is 'w' en kan dus alleen str schrijven.
# 'wb' is de mode die bytes kan schrijven.
new_file = open('nieuw_bestand.txt', 'w')

try:
    print('try: schrijf naar het nieuwe bestand')
    new_file.write(b'dit is geen str, dit zijn bytes')
except TypeError as err:
    print(f'except: {err}')
finally:
    print('finally: sluit altijd het bestand')
    new_file.close()


# ### Oefeningen Exception handling

# Maak een try-except met een `assert` statement die een error geeft.
# Laat de `assert` falen en vang de error op.
# print deze error uit in het `finally` blok van de try-except. 
