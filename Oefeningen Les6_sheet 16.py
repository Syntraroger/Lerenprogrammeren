# Maak een functie balk(b,h,d) de functie geeft de inhoud terug aan het hoofdprogramma
"""def balk(b,h,d):
    return b*h*d

inhoud = balk(2,3,4)
print(inhoud)"""

# Maak een functie tekst_in_kleur(tekst,kleur), kleuren zijn blauw, groen, rood,
# bij een andere invoer wordt de tekst in het wit afgedrukt.
"""from colorama import Fore

def tekst_in_kleur(tekst,kleur):
    if kleur == 'blauw':
        print(Fore.BLUE + tekst + Fore.RESET)
    elif kleur == 'groen':
        print(Fore.GREEN + tekst + Fore.RESET)
    elif kleur == 'rood':
        print(Fore.RED + tekst + Fore.RESET)
    else:
        print(Fore.WHITE + tekst + Fore.RESET)


tekst_in_kleur('dis is ', 'blauw')
tekst_in_kleur('dis is ', 'groen')
tekst_in_kleur('dis is ', 'rood')
tekst_in_kleur('dis is ', 'zwart')"""





# Maak een functie waarin getest wordt of een getal tussen 10 en 100 ligt.

"""def tussen_10_en_100(getal):
    if getal > 10 and getal <100:
        print('Het getal ligt tussen 10 en 100')
    else:
        print('Het getal ligt buiten de range')

tussen_10_en_100(99)"""

# Schrijf een functie een lijst afdrukt van 10 willekeurige getallen tussen 10 en 100.
"""import random

def rand(x):
    lijst=[]
    for i in range(x):
        getal = round(random.uniform(10,100),2)
        lijst.append(getal)
    print(lijst)

rand(10)"""

# Maak een programma waarin de gebruiker de functies van de oppervlaktes kan gebruiken. 1 Vierkant, 2 Rechthoek, 3 Driehoek, 4 Cirkel, 5 Stop
import math

def oppervlakte_vierkant(a):
    return a**2

def oppervlakte_rechthoek(a,b):
    return a*b

def driehoek(a,b):
    return a*b/2

def cirkel(straal):
    return math.pi*straal**2

invoer=''
while invoer != 'stop':
    invoer = input('Welke oppervlakte wil je berekenen vierkant, driehoek, rechthoek, cirkel or type stop ')
    if invoer == 'vierkant':
        a = int(input('Geef de lengte van de zijde aan '))
        opp = oppervlakte_vierkant(a)
        print(opp)
    elif invoer == 'driehoek':
        a = int(input('Geef de basis van de driehoek '))
        b = int(input('Geef de hoogt van de driehoek '))
        opp = driehoek(a,b)
        print(opp)
    elif invoer == 'rechthoek':
        a = int(input('Geef de lengte van de rechthoek '))
        b = int(input('Geef de breedte van de rechthoek '))
        opp = oppervlakte_rechthoek(a,b)
        print(opp)
    elif invoer == 'cirkel':
        a = int(input('Geef de straal in '))
        opp= cirkel(a)
        print(opp)