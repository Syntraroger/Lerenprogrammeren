# Schrijf een functie voor de oppervlakte van een vierkant, rechthoek, driehoek en cirkel.
"""import math

def oppervlakte_vierkant(a):
    return a**2

def oppervlakte_rechthoek(a,b):
    return a*b

def driehoek(a,b):
    return a*b/2

def cirkel(straal):
    return math.pi*straal**2
"""

# Schrijf een functie een naam spelt
"""def spel(naam):

    lijst = []
    for i in range(len(naam)):
        lijst.append(naam[i])

    print(lijst)

spel('roger')"""

# Schrijf een functie dat de x-eerste tekens van een string afdrukt.
"""
def eerste_tekens(string):
    aantal = int(input('hoeveel tekens wil je afdrukken'))
    lijst=[]
    for i in range(aantal):
        lijst.append(string[i])

    print(lijst)

eerste_tekens('delaatstekeer')"""
# Schrijf een functie dat de langste van 2 strings afdrukt, indien even lang drukt hij beide strings zijn even lang

def langste_str(a,b):
    if len(a)>len(b):
        print(a)
    elif len(b)>len(a):
        print(b)
    else:
        print(a, 'en ',b)

langste_str('ser','per')