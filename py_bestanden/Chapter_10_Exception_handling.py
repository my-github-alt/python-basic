#!/usr/bin/env python
# coding: utf-8

# # Exception handling
# 
# `try`  
# `except`  
# `finally`  

# Mensen maken fouten en programmas worden door mensen geschreven.  
# 
# Fouten in een programma kan je opvangen met `try` `except`.  
# De code onder het `try` statement mag een error creëren.  
# Het blokje code onder de `except` statement vangt de gemaakte error op.  
# 
# Normaal stopt het programma bij een error, maar als de error is opgevangen gaat het door.  

# ## try except
# 
# Exception is een _catch-all_, het is de basis van alle Error Exceptions.  
# Als de `assert` statement een `False` expressie ontvangt zal `assert` doormiddel van `raise` een AssertionError geven.  
# Exception zal de AssertionError opvangen.  
# De error-message die opgegeven is bij `assert` is wordt door `except` aan de `err_msg` variabele gegeven.  


try:
    # `raise` express een AssertionError
    fout_waarde = 10 < 0
    assert fout_waarde, 'er is iets fout gegaan'
except Exception as err_msg:
    print(f'error: {err_msg}')

print('na de try-except')


# ### Multiple excepts
# Een stuk code kan meerdere soorten errors geven.  
# Deze kan worden opgevangen door meerdere `except` statements.  
# De `except` statement kan ook meerdere soorten errors opvangen.  

for num in (3, 2, 1, 0):
    try:
        uitkomst = 10 / num
        print(f'10 gedeeld door {num} is: {uitkomst}')
        
    # delen door 0 wordt opgevangen
    except ZeroDivisionError:
        print(f'10 kan niet gedeld worden door 0')
    
    # meerdere errors wordt door deze `except` opgevangen
    except (AssertionError, Exception) as err_msg:
        print(f'log: Er is een onbekende fout opgetreden:\n\t{err_msg}')
        print('stop het programma')
        exit(1)


# ## finally
# Na de `try` en `except` kan er ook een `finally` statement geschreven worden.  
# Dit is optioneel maar al het code in het `finally` blok wordt altijd als laatste uitgevoerd.  
# Het wordt uitgevoerd waneer er een error ontstaat, of de code geen error geeft.  
# De code in het `finally` blok wordt vaak gebruikt om een actie netjes af te sluiten.  
# In het volgende voorbeeld wordt er door `finally` een open file altijd netjes gesloten:  

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
# 
# Maak een try-except met een `assert` statement die een error geeft.  
# Laat de `assert` falen en vang de error op.  
# print deze error uit in het `finally` blok van de try-except.   

