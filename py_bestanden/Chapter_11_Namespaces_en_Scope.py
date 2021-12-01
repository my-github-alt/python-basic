#!/usr/bin/env python
# coding: utf-8

# # Namespaces en Scope

# Python heeft scopes. Scopes zijn verschillende niveas van code.
# Er zijn een paar scopes en die hebben de volgende namen:
# built-in, global en local.

# built-in objecten zijn altijd en overal beschikbaar.
# global objecten zijn in het script aangemaakt en kunnen built-in objecten gebruiken.
# local objecten kunnen built-in en global objecten gebruiken.

# De scopes built-in en global kunnen de objecten in local niet gebruiken of inzien.

# Hieronder een voorbeeld dat de local scope de objecten van de built-in en global scope kan gebruiken.

global_object = "de auto buiten is rood"

def binnen_in_huis():
    # local een nieuw object aangemaakt 
    # dit local object gebruikt de waarde van een global object 
    local_object = f"ik sta binnen (local) en {global_object}"
    # print is een built-in object
    print(local_object)

# roep (global) functie binnen_in_huis
binnen_in_huis()
# print het global object
print(global_object)


# local_object is niet aanwezig in de namespace van de global scope
# Python geeft daarom een NameError
# print(local_object)  # uncomment deze lijn voor de error


# De local scope kan de global objecten negeren en de naam van het object hergebruiken.
# Dit betekend niet dat het global object is aangetast door de local scope.

# Voorbeeld:

global_object = "de auto buiten is rood"

def in_mijn_garage():
    # local een nieuw object aangemaakt
    # het volgende local object overschrijft de verwijzing naar het global object
    global_object = "mijn auto binnen is groen"
    print(global_object)

# roep (global) functie in_mijn_garage aan
in_mijn_garage()
# print het global object
# dit is niet aangepast toen het local is overschreven
print(global_object)


# Het `global` statement kan global objecten binnen laten tot de local scope
# Dan kan het global object local worden aangepast.
# Dit heeft het resultaat dat hierna het global object een andere waarde heeft gekregen.

# Voorbeeld:

global_object = "de auto buiten is rood"

def de_automonteur():
    # Het global statement haalt een global object naar de local scope
    global global_object
    global_object = "de auto is door de automonteur binnen (local) aangepast"

# roep (global) functie de_automonteur aan
de_automonteur()
# print het global object. dit is local aangepast
print(global_object)


# ### Oefeningen Namespaces en Scope

# onderzoek of een `try`-`except` statement een scope bevat.



# onderzoek of een `for`-loop een eigen scope heeft.



# onderzoek of een `if`-`else` statement een eigen scope heeft.



# Check of `global` te gebruiken is in de global scope.
