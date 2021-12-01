#!/usr/bin/env python
# coding: utf-8

# # Classes en functions
# `def` de keyword waarmee een functie wordt aangemaakt.
# `class` de keyword waarmee een class wordt gecreeerd.

# ## def
# `def` is een statement waarmee een functie wordt aangemaakt.
# Een functie is een blokje code wat een set instructies en logica bevat.
# Dit kan meerdere keren in een stuk code gebruikt kan worden.
# print is ook een functie.

def dit_is_een_functie():
    print('print in een functie')


# `call` de functie
dit_is_een_functie()


#
# Functies kunnen ook (meerdere) argumenten ontvangen.
# De argumenten kunnen ook een default waarde hebben.

# Hierinder een functie die de `assert` statement representeerd.
# De functie met de naam `assertion` verwacht 2 argumenten.
# `expression` is een argument en argument `err_msg` heeft een default waarde.

def assertion(expression, err_msg=""):
    if __debug__:
        if not expression:
            raise AssertionError(err_msg)


# ## return
# `return` is een statement die gebruikt wordt in een functie.
# `return` geeft aan welk object de functie terug geeft.
# Als er geen `return` in een functie aanwezig is dan geeft de functie `None` terug.
# Het is good practice als een functie een enkel type object terug geeft.

def is_het_weekend(dag): 
    """ functie die checkt of de gegeven dag in het weekend ligt """
    doordeweeks = {
        "maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"
    }
    weekend = {"zaterdag", "zondag"}
    sdag = str(dag).strip().lower()

    if sdag in doordeweeks:
        # return een bool waarde
        return False
    elif sdag in weekend:
        # return een bool waarde
        return True
    else:
        # geef een error
        raise ValueError(f"gegeven dag ongeldig: {dag!r}")


is_het_weekend('Woensdag')

is_het_weekend('zaterdag')

# is_het_weekend('gehaktdag')


# ## class

# `class` is een statement waarmee een `class` wordt aangemaakt.
# Classes kunnen attributes, properties en methodes bevatten.

# Geinitialiseerde classes hebben een eigen stukje geheugen.
# Er kan dus meerdere van dezelfde class met andere waardes in een stuk code leven.

# Classes zijn hun eigen type.
# Veel van de `built-in` functions zijn achter de schermen een `class`.
# Bijvoorbeeld: `int`, `map`, `range` zijn allemaal een `class`.

# Een stukje uit de python console:
'''
    >>> help(bool)

    Help on class bool in module builtins: 

    class bool(int)
     | bool(x) -> bool
     |
     | Returns True when the argument x is true, False otherwise.
    ...
'''

# Hieronder een voorbeeld van een class met een methode dat het memory adres uitprint.


class EenClass:
    def print_adres(self): 
        print(f"deze class heeft de memory adres: {id(self)}")

# initializeer 2x de class EenClass
een1 = EenClass()
een2 = EenClass()

# print het addres met de methode in de class
een1.print_adres()
een2.print_adres()


# De methode in de class heeft een argument: self
# self verwijst naar het memory-adres van de class.
# De variable waaraan de class is geinitializeerd verwijst ook naar dat memory-adres.

# In de class kan self ook gebruikt worden om onderdelen van de class op te vragen en/of aan te roepen.
# Als de class is geinitialiseerd dan kan de attribute ook worden opgevraagd of aangepast.

# Voorbeeld hieronder

class VoorbeeldSelf:

    een_attribute = "dit is een attribute"
    def get_attribute(self):
        return self.een_attribute

    def print_attr(self, uppercase=False):
        attr = self.get_attribute()
        if uppercase:
            # maak van attr allemaal hoofdletters
            attr = str(attr).upper()
        print(attr)


# initializeer 2x de class VoorbeeldSelf
voorbeeld1 = VoorbeeldSelf()
voorbeeld2 = VoorbeeldSelf()

# print de class attribute
voorbeeld1.print_attr()


# variable voorbeeld2 kan gezien worden als de self in de class
voorbeeld2.een_attribute = "van buiten aangepast"
# print de class attribute
voorbeeld2.print_attr(uppercase=True)


# Het is mogenlijk om een class, zoals functies, parameters te geven.
# Dit gebeurt met de speciale methode __init__

# Voorbeeld:

class Login: 
    """ voorbeeld 'login' class """
    def __init__(self, username, password="Sup3rS3cret!"):
        self.username = username
        self.password = password

    def click_submit(self):
        print(f"press submit button")

    def do_login(self, press_submit=False):
        print(f"fill username input: {self.username}")
        print(f"fill password input: {self.password}")
        if press_submit:
            self.click_submit()


login_page = Login("Henk123", "password1")
login_page.do_login(press_submit=True)


# ### Oefeningen Classes en functions

# * Maak een `class` genaamd Hond.
# * Geef de `class` een attribute dat aangeeft hoeveel poten een hond heeft.
# * Zorg met de `__init__` methode dat een hond een naam kan krijgen.
# * Maak een methode in de `class` waarmee de hond kan blaffen.

