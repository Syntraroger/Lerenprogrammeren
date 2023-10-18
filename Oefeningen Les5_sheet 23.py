# Maak een functie maaltafel. Geef de maaltafel mee als parameter. Hierna krijg je de vermenigvuldigingen 100.

"""def maaltafel(x):
    for i in range (1,101):
        print(i, 'x', x, '=', i*x)


maaltafel(int(input("Geef de maaltafel mee ")))"""



# Maak een functie balk(b,h,d) de functie geeft de inhoud terug aan het hoofdprogramma

"""def balk(b,h,d):
    inhoud = b*h*d
    return inhoud

z = balk(2,3,4)
print(z)"""




# Maak een functie tekst_in_kleur(tekst,kleur), kleuren zijn blauw, groen, rood,
# bij een andere invoer wordt de tekst in het wit afgedrukt.
from colorama import Fore
def tekstkleur(tekst, kleur):
    if kleur == 'RED':
        print(Fore.RED+str(tekst)+Fore.RESET)
    elif kleur == 'BLUE':
        print(Fore.BLUE + str(tekst) + Fore.RESET)
    elif kleur == 'GREEN':
        print(Fore.GREEN + str(tekst) + Fore.RESET)
    else:
        print(Fore.LIGHTWHITE_EX + str(tekst) + Fore.RESET)


tekstkleur('deze tekst rood', 'RED')
tekstkleur('deze tekst blauw', 'BLUE')
tekstkleur('deze tekst groen', 'GREEN')
tekstkleur('deze tekst is anders', 'BLACK')
"""

# Maak een functie waarin getest wordt of een getal tussen 10 en 100 ligt.

"""def getal(x):
    if x > 10 and x <100:
        print('Het getal ligt tussen 10 en 100, namelijk ', x)
    else:
        print('Het getal ligt buiten de range')



getal(55)"""