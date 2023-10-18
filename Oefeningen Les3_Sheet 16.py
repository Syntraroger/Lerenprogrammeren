# Schrijf een programma hoeveel het kost om een volle tank te vullen rond af op 2 cijfers na de komma
"""brandstof = input('Welke brandstof gebruikt u diesel of benzine?')
aantal_liters= float(input('Hoeveel liter heeft u getankt?'))

if brandstof.lower()=='benzine':
    print('Prijs volle tank benzine is', round((aantal_liters*1.55),3))
elif brandstof.lower()=='diesel':
    print('Prijs van een volle tank diesel is',round((aantal_liters* 1.2),3))"""


# Schrijf een programma dat euro omzet naar Dollar, afronden op 3 cijfers na de komma

"""
hoeveelgeld = float(input('Hoeveel geld wilt u omzetten'))
valuta = input('Wilt u omzetten naar euro of dollar?')

if valuta.lower() == "dollar":
    print('Het bedrag in dollar is', round(hoeveelgeld *1.2, 2))
elif valuta==str('euro'):
    print('Het bedrag in euro is', round(hoeveelgeld*0.8,2))
"""

# Schrijf een programma dat de lengte van 2 stukken tekst berekent.

"""
tekst_1 = str(input('Geef de eerste tekst in '))
tekst_2 = str(input('Geef de tweede tekst in '))

Lengte_Tekst_1 = len(tekst_1)
Lengte_Tekst_2 = len(tekst_2)

print(f'De lengte van de eerste tekst is {Lengte_Tekst_1} en de lengte van de tweede tekst is {Lengte_Tekst_2}')
"""

# Schrijf een programma dat de eerste 2 letters van de voornaam en achternaam samenvoegt.

"""
voornaam = str(input('Geef de voornaam in '))
achternaam = str(input('Geef de achternaam in '))

voornaam,achternaam = voornaam.replace(" ", ""),achternaam.replace(" ", "")
x = voornaam[0:2]+achternaam[0:2]
print(x)"""