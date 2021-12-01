#!/usr/bin/env python
# coding: utf-8

# # Importing modules
# `import` ...
# `from` ... `import` ...
# `import` ... `as` ...
# `from` ... `import` ... `as` ...


# importeer de module time
import time

# vraag de huidige tijd op
time_before = time.asctime()

# wacht voor 3 seconden en vraag opnieuw de tijd op
time.sleep(3)
time_after = time.asctime()

# print de tijden
print(time_before)
print(time_after)


# Er kan ook specifiek aangegeven worden wat je wil importeren uit een module.
# Op deze manier wordt wat je heb geimporteerd direct aan de huidige namespace toegevoegd.

# van module: math, importeer pi en tau
from math import pi, tau

# check dat 2 * pi gelijk is aan tau
assert 2 * pi == tau, "error msg: 2 * pi is niet gelijk aan tau"


# Ook kan je code importeren en gelijk een andere naam gegven voor in de namespace geven.
# hiervoor gebruik je het keyword `as`.

from pprint import pprint

# ascii_lowercase is hernoemd naar alphabet
from string import ascii_lowercase as alphabet

# pretty-print een lijst met letters
pprint(list(alphabet))


# ### Oefeningen Importing modules
# Bekijk de modules van Python op deze website:
# https://docs.python.org/3/py-modindex.html

# Een greep uit de lijst van modules:
# csv  https://docs.python.org/3/library/csv.html - lezen en schrijven van Comma Separated Values (CSV) files.
# datetime  https://docs.python.org/3/library/datetime.html - tijd en datum manipulatie.
# logging  https://docs.python.org/3/library/logging.html - schrijf debug informatie en errors naar een file.
# pathlib  https://docs.python.org/3/library/pathlib.html - _cross platform_ file navigatie, gebruiksvriendelijker dan os.path.
# tempfile  https://docs.python.org/3/library/tempfile.html - maak een tijdelijke file aan die na gebruik zichzelf deletet.

# Test modules van python:
# doctest  https://docs.python.org/3/library/doctest.html - een unittest module waar documentatie van de functie de test bevat.
# unittest  https://docs.python.org/3/library/unittest.html - de unittest module (gebaseerd op Java's JUnit).



# Bekijk wat `import this` doet
