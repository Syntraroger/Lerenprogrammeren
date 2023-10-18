# Alle mannen ouder dan 20 jaar, in genk met een rijbewijs.
# Maak een functie die dit test


"""def check():
    leeftijd = int(input('Hoe oud bent u :'))
    man= input('Bent u een man, ja of nee ')
    wnpl = input('Geef uw woonplaats in ')
    rijb = input('Heeft u een rijbewijs, ja of nee ')
    if (leeftijd > 20 and man.lower()== 'ja' and wnpl.lower() == 'genk' and rijb.lower()== 'ja'):
        print('U hoort bij onze geselecteerde groep')
    else:
        print('U hoort niet bij de geselecteerde group')


check()"""

# Test of een getal deelbaar door 4 of door 3 is.
# Indien waar print het dubbel in het groen, indien onwaar toon het getal in het rood.

from colorama import Fore

def deelbaar(x):


    if x%3==0 and x%4==0:
        print(Fore.GREEN + str(2*x) + Fore.RESET)
    else:
        print(Fore.RED + str(x) + Fore.RESET)


deelbaar(12)

deelbaar(8)

