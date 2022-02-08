#!/usr/bin/env python
# coding: utf-8

# # Boolean values
# 
# Een boolean is `True` of `False` 
# 
# Een vergelijking dat waar is heeft een `bool` met de waarde `True` .  
# Iets dat niet waar is heeft de `bool` waarde `False` .  
# 
# `None` representeerd de afwezigheid van een waarde.  
# De `bool` waarde van afwezigheid is `False`.  
# 
# `0` is de afwezigheid van een getal.  
# `[]` is een lege lijst waar waardes afwezig zijn.  
# `{}` is een lege dict waar waardes afwezig zijn.  
# ...  
# Elke lege data container is een `False` boolean value.  

bool("")

# Python heeft naast `True` en `False` ook `None`.  
# `None` geeft aan dat een waarde er (nog) niet is, het is een placeholder.  
# Functies die niet specifiek een waarde terug geven, geven dan altijd een `None` terug.  
# Omdat `None` een lege plek voorsteld is de boolean waarde van `None` altijd `False`.  

een_variable = None  # `een_variable` kan later in het script een andere waarde krijgen.  
bool(een_variable)

# append geeft geen nieuwe lijst terug, maar een `None`
dit_is_none = list().append(1)
repr(dit_is_none)

# ###  Oefeningen Boolean values

# Wat zijn de `int` waardes van `True` en `False` ?


# Wat is de `bool` waarde van de string (`str`) `"False"` ?

false: str = "False"
# bool van `false` ?


# Wat is de waarde dat je van de functie `print()` terugkrijgt ?


# [`assert`] is een statement dat test of de expressie `True` is.  
# Als de expressie `False` is is het een [`AssertionError`] en stopt het Python script gelijk.  
# 
# > `assert` expressie  
# 
# of  
# 
# > `assert` expressie, 'errormessage'

# voorbeeld assert
assert bool('dit geeft een boolean terug'), 'dit is een error message'


# Maak een `assert` die checkt of `True` van het type `bool` is. Doe dit ook voor `False`.  


# Maak een `assert` die checkt of `True` gelijk is aan 1 en een die `False` gelijk is aan 0.

