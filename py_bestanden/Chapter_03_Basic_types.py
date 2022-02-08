#!/usr/bin/env python
# coding: utf-8

# # Basic types
# In Python is alles een object.  
# De objecten zoals `1` or `'Hallo'` hebben types.  
# Python bepaald dynamisch welk type een object heeft.  
# 
# Hieronder wordt een paar veelgebruikte types uitgelegd.  

# ## Int
# `int` representeerd volledige getallen zoals: `-1`, `0`, `1` ... `10000`, etc.   

een = 1
twee = 2
een + twee


# De functie `int` kan objecten dat een getal representeert omzetten naar een integer getal

# +100 is een string
positief = "+100"
int(positief)

# -200 is een string
negatief = "-200"
int(negatief)


# `int` kan gebruikt worden om hexadecimaal of _base2_ getallen omzetten naar een decimaal getal

# omzetten binair getal naar decimaal
binair = '110'
int(binair, 2)

# omzetten hexadecimaal getal naar decimaal
hexadecimaal = '1A'
int(hexadecimaal, 16)


# ## Float
# `float` representeerd een zwevend komma getal  
# De functie `float` kan objecten die een getal representeren omzetten naar een kommagetal
# 
# `float` word [inair anders geintrepeteerd van een decimaal getal.  
# Er is daar dan ook een standaard voor gemaakt (IEEE_754).  
# Door het precisie element in kommagetallen kunnen er floatingpoint errors ontstaan.  

# zou 0.9 moeten zijn
0.3 + 0.3 + 0.3


# `float` kan objecten die een getal representeren omzetten naar een kommagetal

# '-200' is een string
negatief = "-200"
float(negatief)

# '+100' is een string
positief = "+100"
float(positief)

# wetenschappelijke notatie van 0.00001
wetenschappelijke_notatie = "1e-05"
float(wetenschappelijke_notatie)

# een int naar float  plus  een wetenschappelijke notatie als float
float(10_000) + float(wetenschappelijke_notatie)

# `int` en `float` kan samen gebruikt worden in sommen

0.618033 + 1


# ## Str
# Elke normale string in Python3 is een unicode string.  
# 
# `str` is een type dat een _string_ aan characters representeerd.  
# Dit kan een enkele character zijn: `'A'`  
# Of meerdere `'ABC'`  
# Omdat een `str` dus unicode characters zijn kan het ook emoji's bevatten. 

emoji_str = "\N{BLACK SUN WITH RAYS} zon en bloem ⚘"
emoji_str

# Zoals er bij `int` is laten zien kan een `str`  object worden omgezet naar `int`  
# Vrijwel alles in Python kan omgezet worden naar `str`  
# 
# Strings kan ook geformateerd worden met waardes er in.
# Met een `f` voor het begin van een string wordt de string een f-string 
# Accolades kunnen dan in de f-string gebruikt worden om een object in een string te weergeven.

one_million = 1_000_000
str_million = str(one_million)
f'{str_million} of type str: {isinstance(str_million, str)}'


# ### Oefeningen Basic types
# 
# Maak een string aan dat een getal is en probeer dat met een andere string op te tellen.  
# voorbeeld: `'1' + 2`

# Probeer een string te vermenigvuldiggen.  
# voorbeeld `'a' * 100`

# Maak een willekeurige som met een `float` en een `int`
