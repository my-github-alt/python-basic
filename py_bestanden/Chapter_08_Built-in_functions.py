#!/usr/bin/env python
# coding: utf-8

# # Built-in functions
# Python heeft veel built-in functions
# Deze functies zijn overal ten alle tijden en in elke scope te gebruiken.
# Het zijn geen keywords dus de functies kan overschreven worden door een variabele of functie hetzelfde te noemen.

# overschrijf de built-in functie: `filter`.
print(filter)
filter = "filter is geen functie meer"
print(filter)


# Hieronder een kleine selectie van functies die belangrijk en/of hulpzaam zijn.

# ### help
# `help` is een built-in interactieve documentatie viewer.
# `help` zonder agrumenten start een interactieve sessie.  Dit werkt het beste in een Python console.
# Om uit de interactieve sessie te komen kan er `quit` worden getyped.

# `help` met een object als argument laat de documentatie/class of functue van het gegeven object zien.
# `help` werkt ook met third-party libraries zoals selenium.

# help(dir)   # uncomment 


# ### dir
# `dir` geeft altijd een lijst van strings terug.  
# `dir` zonder argumenten heeft de huidige variabelen van de huidige scope.  
# `dir` met een object als argument geeft een lijst met alle attributen van dat object terug.

print(dir(str))

local_var = None
print(dir())
print('local_var' in dir())


# ### type
# `type` verwacht een object als argument en geeft dan het type van het object terug.

een_string = "dit is een string"
type(een_string)

type(print)


# ### print
# `print` is een handige functie die de gegeven argumenten _uitprint_ in de console.
# Alles kan worden uitgeprint met `print`.
# `print` heeft een aantal _keyword arguments_ waarmee de printfunctie kan worden aangepast.

lijst = ['b', 'c']
print('a', lijst, {'d': 'e'}, sep=' !! ', end='\n\n double newline \n\n')


# ### range
# `range` is een functie die een reeks aan getallen voorsteld.
# `range` wordt vaak gebruikt in loops.
# `range` is een luie functie.
# Dit betekend dat range pas een nummer geeft als de code er om vraagt.

# range doet op zichzelf niks
print(range(10))

# maak een lijst met range van 0 tot 10
print(list(range(10)))

# maak een lijst met range van 1 tot 10 in stappen van 2
print(list(range(1, 10, 2)))


# ### open
# `open` is een functie die files kan openen/aanmaken waarna deze aan te passen zijn.
# Nadat een file is geopend moet deze ook gesloten worden met `.close()`.
# Als de file niet netjes wordt gesloten kan het voorkomen dat deze file corrupt raakt.

# open een file in mode: write
open_file = open('new_file.txt', mode='w')
open_file.write('text in een nieuw bestand\n')
# sluit de file
open_file.close()



# ### Oefeningen Built-in functions

# Opdracht 1:  
# Bekijk de built-in functions pagina https://docs.python.org/3/library/functions.html
# Onderzoek welke built-in functie een lengte van een object terug geeft



# Opdracht 2:
# Bekijk de help text van range
# Maak met range’s start, stop en step argumenten een lijst zoals deze: `[0, 25, 50, 75, 100]`
