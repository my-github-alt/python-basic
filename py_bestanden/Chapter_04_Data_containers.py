#!/usr/bin/env python
# coding: utf-8

# # Data containers
# In Python zijn data containers objecten die een serie verwijzingen naar objecten representeerd.  
# 
# De verschillende containers hebben elk een andere eigenschap.  
# Er zijn 2 kenmerken van data die de eigenschappen onderling de data containers bepalen.  
# Immutable objecten: Data die niet aangepast kan worden, alleen overschreven.  
# Mutable objecten: Data die aangepast kan worden.  
# 
# De eerste positie in series zoals `list` `str` `tuple` is een 0

# ## List
# `list` is een mutable data container die mutable en immutable data kan vasthouden.  

# een `list` heeft de volgende functies die gebruikt kan worden
print([_ for _ in dir(list) if not _.startswith('_')])


# `append` voegt een enkel object toe aan de lijst.  
# `extend` voegt de objecten uit een ander gegeven lijst toe aan de lijst.  
# `index` zoekt het gegeven object in de lijst en geeft een nummer terug.  
# `pop` haalt een object uit een lijst.  

lijst_1 = [1, 2, 3]
lijst_1.append(4)   # voeg 4 toe aan lijst_1
print(lijst_1)

lijst_2 = ['a', 'b', 'c', 'a']
index_a = lijst_2.index('a')  # krijg de eerste index van 'a'
print(index_a)

# haal het object op index 0 uit de lijst_2
pop_0 = lijst_2.pop(0)
print(f'{pop_0!r} is ge-popped uit lijst_2')
print(lijst_2)

lijst_3 = [9, 8.0, '7']
lijst_1.extend(lijst_3)   # voeg alle objecten van lijst_2 toe aan lijst_1
print(lijst_1)

lijst_1[0] = 1_000  # overschrijf het eerste object in de lijst_1 [0]
print(lijst_1)

# `append` en `extend` geven geen nieuwe lijst terug, deze functies passen alleen de lijst aan.  
# Soms is het wenselijk om lijsten te combineren en een nieuwe lijst te creëren.  
# Dit kan met de `+` operator.

list_a = ['a']
list_b = list('b')
list_abc = list_a + list_b + ['c']
print(list_abc)


# ## Tuple
# `tuple` is een immutable data container die _mutable_ en immutable data kan vashouden.  
# Een tuple kan gehashed worden tenzij een tuple een immutable object bevat.

# een tuple heeft de volgende functies die gebruikt kan worden
print([_ for _ in dir(tuple) if not _.startswith('_')])


# `count` tel hoeveel het gegeven object voorkomt in de tuple  
# `index` zoekt het gegeven object in de tuple en geeft een nummer terug  

tuple_1 = (1, 2, 3)
tuple_2 = ('a', 'b', 'c')
tuple_3 = tuple_2 + tuple_1 + tuple_2   # voeg verschillende tuples aan elkaar toe om een nieuwe tuple te maken
print(tuple_3)

# vraag op waar de eerste 2 staat in de tuple
index_2 = tuple_1.index(2)
print(index_2)

# hoe vaak komt 'a' in de tuple voor
amount_a = tuple_3.count('a') 
print(amount_a)

# hash van een tuple
print(hash((1, 2, 3)))
print(hash((1, 2, 4)))


# ## Set
# `set` is een mutable data container die alleen immutable data kan vasthouden.  
# Een `set` is een data container die alleen unieke waardes bevat.  
# Een `set` kan alleen objecten bevatten die gehashed kan worden.  

# een set heeft de volgende functies die gebruikt kan worden
print([_ for _ in dir(set) if not _.startswith('_')])

# `add` voegt een enkel object toe aan de set.  
# `difference` geeft het verschil terug uit twee sets.  
# `pop` haalt een willekeurig object uit de set.  
# `update` voeg een andere set toe aan de set.  

lijst = [3, 2, 1, 'a', 'c', 'b']
set_1 = set(lijst)  # convert lijst naar set
print(set_1)

set_2 = {1, 2, 3}   # maak een set 
diff_set_1 = set_1.difference(set_2)  # verschil van set_1 en set_2
print(diff_set_1)

set_2.add(2)
print(set_2)

set_3 = {5, 1, 4, 2, '3', 6}   # maak een set 
set_2.update(set_3)
print(set_2)

# `update` geeft geen nieuwe set terug.  
# Soms is het wenselijk om twee set's bij elkaar toe te voegen en een nieuwe aan te maken.  
# Dit kan met een `|` (union operator)

set_a = {'a'}
set_b = set('ab')
set_abc = set_a | set_b | set('c')
print(set_abc)

# ## Dict
# `dict` is een mutable data container die immutable data gebruikt om naar mutable of immutable data te verwijzen.  
# Een `dict` is een object met een key-value pair data structuur.  
# Het is te vergelijken is met JSON
# 
# In een dict kan de value elk Python object zijn.  
# In een dict kan de key alleen objecten bevatten die gehashed kan worden.
# 
# Een key-value pair kan vergeleken worden met een tafel in een database (excel sheet).  
# De kolommen zijn de keys en de waarde er onder zijn de values 

# een dict heeft de volgende functies die gebruikt kan worden
print([_ for _ in dir(dict) if not _.startswith('_')])


# `keys` geeft een lijst met alle keys terug  
# `values` geeft een lijst met alle values terug  
# `get` geeft een value terug van de opgevraagde key  
# `items` geeft een lijst met de key-value paar in een tuple terug: `[('key', 'value'), ... ]`  
# `update` voeg een andere dict toe aan de dict, overschrijft de bestaande waardes.  

dict_1 = {'key1': 'value1', 2: 'two'}  # maak een dict aan
dict_1[3] = 'three'  # voeg key  3  met value 'three'  toe aan de dict
print(dict_1)

value = dict_1.get(4)  # vraag 4 op die niet in de dict bestaat
print(value)  # None

dict_2 = {'key1': 'value from dict_2'}
dict_1.update(dict_2)  # overschrijf de value van een bestaande `key1` met update
print(dict_1)

dict_1[2] = 'TWO'  # overschrijf met subscription 
print(dict_1)

# Soms is het wenselijk om twee dicts's bij elkaar toe te voegen en een nieuwe aan te maken.  
# Dit kan met een `|` (union operator)

dict_a = {'a': 'A'}
dict_b = dict(b='B')
dict_abc = dict_a | dict_b | {'c': 'C'}  # mogenlijk sinds Python3.9
print(dict_abc)


# ### Oefeningen Data containers
# De oefeningen vragen om de type van het object te testen met [`isinstance`].  
# `isintance` geeft een `True` of `False` terug.  
# Zie hieronder hoe deze functie gebruikt wordt.
# 
# > `isintance(object, type)`

# voorbeeld isinstance
obj = 1
print(isinstance(obj, int))


# Maak een `list` aan en voeg er objecten aan toe.  
# Voeg andere objecten toe met `append`.  
# Check wat voor objecten de `list` heeft met `print`.  
# Check met `isinstance` of de `list` ook een `list` is.  


# Maak een `tuple` aan met een paar objecten.  
# Voeg andere objecten toe aan de `tuple`.  
# Check wat voor objecten de `tuple` heeft met `print`.  
# Check met `isinstance` of de `tuple` ook een `tuple` is.  


# Maak een `set` aan met een paar objecten.  
# Voeg andere objecten toe aan de `set` met `add`.  
# Check wat voor objecten de `set` heeft met `print`.  
# Check met `isinstance` of de `set` ook een `set` is.  


# Maak een `dict` aan met een paar objecten.  
# Voeg andere objecten toe aan de `dict`.  
# Voeg andere objecten toe aan de `dict` met `update`.  
# Check wat voor objecten de `dict` heeft met `print`.  
# Check met `isinstance` of de `dict` ook een `dict` is.  


# Schrijf Python code dat de volgende stappen bevat:
# 1. maak een lijst aan met de naam lijst_1
# 2. maak een lijst aan met de naam lijst_2 die lijst_1 bevat
# 3. gebruik append om lijst_2 aan lijst_1 toe te voegen
# 4. bekijk wat lijst_1 bevat
