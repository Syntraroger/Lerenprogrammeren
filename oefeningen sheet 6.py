# Schrijf een programma  100x een ingeven getal vermenigvuldigt.

"""getal = int(input('Geef een getal '))

for i in range (1,101):
    print(getal*i)"""

# Schrijf een programma 10 keer de machten van het getal 2 wordt weergegeven.
"""getal = 2

for i in range(1,11):
    print(getal**i)
  """

# Schrijf een programma dat 5 ingegeven getallen met elkaar optelt.
"""som=0
for i in range (0,5):   # kan ook range (0,5) of range (5)
    getal= int(input('Geef een getal in '))
    som += getal

print(som)"""

# Schrijf een programma dat grootste ingegeven getal van 10 getallen weergeeft.

"""grootste =0
for i in range (0,10):
    getal = int(input('Geef een getal in '))

    if (getal>grootste):
       grootste=getal
print(f'Het grootste getal is {grootste}')"""


# Zelfd opgave maar nu met een lijst

lijst_getallen = []
for i in range(10):
    getal = int(input('Geef getal in'))
    lijst_getallen.append(getal)
print(max(lijst_getallen))             #vervang max voor min door laagste getal weer te geven in de lijst

#-----------------------------------------------
#  Parameter bestaat alleen in de functie.
#  Met return kan ik de waarde doorgeven van de functie naar het hoofdprogramma
"""def doe_iets(x):
    y=x*2
    print(y)"""
#______________________________________________
# AFdrukken van uit functie gebruik een PRINT
# Wil je de waarde doorgeven gebruik dan een RETURN

