#!/usr/bin/env python
# coding: utf-8


# Hoe gebruik ik Python om een request te maken naar een API
# Een gebruiksvriendelijke module om internet verkeer tot stand te brengen komt niet met Python mee geinstalleerd.
# Er zijn externe modules die dit beter kunnen doen, deze zijn gewoon met PIP te installeren.

# Maar een request maken zonder dependencies is wel mogenlijk, maar het is langdradig ofwel verbose.
# Hieronder een voorbeeld.

from http.client import HTTPResponse
from urllib.parse import urlencode, urlunparse, ParseResult, parse_qsl
from urllib.request import Request, urlopen


# Uitendelijke url:
#   https://wttr.in/Veenendaal?m2&F&A&lang=nl

# query codes zijn hier uitgeschreven:  https://wttr.in/:help
query: dict = {
    'm': '',        # metric (SI)
    '2': '',        # current weather + today's + tomorrow's forecast
    'F': '',        # do not show the "Follow" line
    'A': '',        # ignore User-Agent and force ANSI output format (terminal)
    'lang': 'nl'    # Localization
}

# creëer de url
url: str = urlunparse(ParseResult(
    scheme   = 'https',
    netloc   = 'wttr.in',
    path     = '/Veenendaal',
    query    = urlencode(query),    # parse de dict naar een query url part
    params   = None,
    fragment = None,
))

# maak een request aan
request = Request(url, method='GET')

# verstuur het request
response: HTTPResponse = urlopen(request)

# check of de request door de server succesvol is afgehandeld
assert response.code == 200

# lees de data uit de response
data = bytes.decode(response.read())

# weergeef de data
print(data)
print('= ' * 60)


# Betere modules om requests mee te maken
# requests is de meest gebruikte module om met Python het internet op te gaan.
# Het is een module die niet asynchroon kan worden gebruikt.
# httpx is een andere module voor om requests te maken die wel asynchroon gebruikt kan worden.

# In dit chapter houden we het gemakkelijk en synchroon door requests te gebruiken.

import requests
from requests import Response

# verstuur het request
res: Response = requests.get('https://wttr.in/Veenendaal', params={'m': '', '2': '', 'F': '', 'A': '', 'lang': 'nl'})

# check of de request door de server succesvol is afgehandeld
assert res.ok

# weergeef de data
print(res.text)



# Testen maken in Python
# Python heeft zelf een aantal modules (unittest doctest) waarmee je testen kan maken.

# De unittest module is oud, ouder dan PEP-8, en gebaseerd op de unittest library van Java: JUnit.
# Om een simpele testcase te maken moet je gebruik maken van inheritance.

# Doctest wordt gebruikt om programeer snippets in docstrings te testen.
# De doctest gimmick is niet handig te gebruiken bij grotere testcases.

# De meest gebruikte Third-party library om met Python te testen is pytest.
# Deze module is ook gewoon met PIP te installeren.
# De testcases in pytest is een functie waarvan de naam begint met test.
# En met pytest kan je waardes gewoon met assert testen.

# Voorbeeld van een unittest met pytest.

import pytest


def keer_twee(nummer: int) -> int:
    return int(nummer) * 2

# # Uncomment de onderstaande functie om deze te testen

# def test_dupliceer_2_en_1_is_6():
#     given = keer_twee(2)  # 2 * 2 = 4
#     expected = 4
#     assert given == expected, f"Error {given = } {expected = }"


pytest.main(['--verbosity=1'])



# Oefeningen API testen met Python

# Test de API van deckofcardsapi.com.
# Maak API tests op basis van de testcases.
