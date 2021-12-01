#!/usr/bin/env python
# coding: utf-8

# # Operators
# Het gebruik van tekens en/of keywords om expressies te maken.

# ## Comparison operators
# Ook wel relational operators) genoemd.

# Deze operators worden veelal gebruikt met cijfers.

# `<` kleiner dan.
# `>` groter dan.
# `==` is gelijk aan.
# `>=` groter of gelijk aan.
# `<=` kleiner of gelijk aan.
# `!=` niet gelijk aan.

print(1 < 2)   # 1 is kleiner dan 2


print(2 > 1)   # 2 is groter dan 1


print(3 == 3)   # 3 is gelijk aan 3


print(4 >= 4)   # 4 is groter of gelijk aan 4


print(5 <= 6)   # 5 is kleiner of gelijk aan 6


print(6 != 7)   # 6 is niet gelijk aan 7


# Ook strings kunnen gebruikt worden in Comparison operators

een_string = "A"
print('a' == een_string.lower())


# #### Chained operators
# De comparison operators kunnen ook aan elkaar geregen worden.

# De expressie  
#     `1 < 2 and 2 < 3 and 3 <= 4`  
# kan geschreven worden als  
#     `1 < 2 < 3 <= 4`

print(1 < 2 < 3)

print(2 > 1 > 0)

print(3 == 3 != 4)

print(4 >= 3 <= 4)

print(5 <= 5 <= 6)

print(6 != 7 == 7)


# ## Membership operator
# `in` is het keyword dat gebruikt wordt om de _membership_ van een object te testen.

# Met `in` kan je testen of een waarde voorkomt in een data container zoals een `list`, of de keys van een `dict`.
# Maar ook, zoals hieronder, een woord in een zin.


woord = "Python"
zin = "Test de membership van objecten met Python"

# Test dat het woord voorkomt in de zin
print(woord in zin)


nummer = 2
tuple_met_cijfers = (1, nummer, 3)

# Test dat nummer 2 voorkomt in de tuple met cijfers
print(2 in tuple_met_cijfers)


# ## Identity operator
# `is` is het keyword dat gebruikt wordt om de identiteit van twee objecten te vergelijken.

# Python gebruikt onder de 'motorkap' de taal 'C' om de computer aan te sturen.
# De objecten van Python worden opgeslagen in het werkgeheugen van de computer.
# Deze objecten hebben een memory-adres waarmee ze naar hun waarde verwijzen.

# Met de `id` functie kan de het adres worden opgevraagd.

# `is` vergelijkt de addressen van de objecten in het werkgeheugen. 
# `obj is obj` is te vergelijken met `id(obj) == id(obj)`


# `is` wordt veel gebruikt om  te checken of een variabele `None` is.
# `None` is een singleton, wat betekend dat er maar één van is.

verwijzing_naar_none = None
print(verwijzing_naar_none is None)

# Elke functie die geen `return` heeft, geeft None terug.
result_print = print('dit is geprint')
print(result_print is verwijzing_naar_none)

# Voorbeeld dat None een singleton is, en dus naar hetzelfde adres verwijst.
id_verwijzing_naar_none = id(verwijzing_naar_none)
id_result_print = id(result_print)

print(id_verwijzing_naar_none)   # print uit de adressen van de variables
print(id_result_print)

print(id(verwijzing_naar_none) == id(result_print))


# Python probeert zo efficient mogenlijk te zijn en verwijst eerder naar objecten dan dat er nieuwe wordt aangemaakt.

# Hoe verwijzingen het origineel kan aanpassen.
dict_1 = {'key': 'value'}
dict_2 = dict_1
dict_3 = dict_1.copy()  # gebruik de `copy` functie van dict

del dict_2['key']  # delete de key uit dict_2
print(dict_1)  # check de inhoud van dict_1

print(dict_3)  # check de inhoud van dict_3

# hieronder de expressie die test welke dicts naar elkaar verwijzen.
print(dict_1 is dict_2 is not dict_3)


# ## Boolean operators
# `and`
# `or`
# `not`

# variabelen voor de voorbeelden hieronder
kleur_auto_1 = 'rood'
kleur_auto_2 = 'groen'

# ### and
# De `and` geeft aan dat er meerdere expressies waar moet zijn om een `True` terug te krijgen.  
# Als er ook maar één van de expressies onwaar is wordt het als een `False` beschouwd.  


# beide expressies moeten `True` hebben om `True` te krijgen
print(kleur_auto_1 == 'rood' and kleur_auto_2 == 'groen')  # True

print(kleur_auto_1 == 'rood' and kleur_auto_2 == 'paars')  # False

# ### or
# De `or` geeft aan dat een enkele expressies waar moet zijn om een `True` terug te krijgen.  
# De expressie wordt `False` als alle expressies onwaar zijn.  

print(kleur_auto_1 == 'oranje' or kleur_auto_2 == 'groen')  # True

print(kleur_auto_1 == 'oranje' or kleur_auto_2 == 'paars')  # True


# ### not
# De `not` geeft aan dat de expressie onwaar moet zijn om een `True` te worden.
# `not True` is `False` en `not False` is `True`

bool_1 = kleur_auto_1 == 'oranje'  # False
bool_2 = kleur_auto_2 == 'groen'  # True
print(not bool_1 and bool_2 ) # True

value = None
print(value is not None)



# ### Oefeningen Operators

# ### Chained operators opdracht
# Pas de variabelen  `x`, `y` en `z`  zo aan dat er geen `AssertionError` meer voorkomt.

x = -5
y = 500
z = 100

# hieronder een ketting aan comparisons 
boolean_value = bool(x >= 0 < y < 100 < z) 
assert boolean_value, f"{x} >= 0 < {y} < 100 < {z}"



# ### Membership operator opdracht
# Pas de `assert` hieronder aan zodat deze geen `AssertionError` meer geeft.

een_dict = {"key": "value", "andere_key": "andere_value"}
err_msg = "dit gaat fout omdat 'in' de keys van de dict bekijkt. gebruik een_dict.values()"

# zorg dat deze assert statement geen error geeft
assert "value" in een_dict, err_msg



# ### Identity operator opdracht
# Gebruik het `is` statement om te testen welke van de volgende lijsten naar elkaar verwijzen

lijst_1 = ['a', 'b', 'c']
lijst_2 = lijst_1
lijst_3 = lijst_1.copy()
