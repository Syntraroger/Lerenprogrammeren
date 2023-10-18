# Simuleer een factuur waarin de gebruiker een product en prijs ingeeft.
# Op het einde wordt het factuur bedrag berekend


"""artikelnummer = ('')
prijs = 0

while(not artikelnummer == 'stop'):
    artikelnummer = input('Geef een artikelnummer in of typ stop ')
    if(artikelnummer == 'stop'):
        break
    else:
        try:
            prijs = prijs + float(input(f'Geef de prijs in voor artikel {artikelnummer} '))

        except ValueError:
            print("gelieve een  getal in the geven ")

print("Het factuurbedrag is: ",prijs)"""
import random

# Schrijf een programma dat 10 willekeurige getallen geeft van 1 tot 100,
# geef weer hoeveel getallen kleiner zijn dan 30 tussen de 30 en de 60 en groter dan 60.
"""
import random

i=0
klein30 = 0
tussen = 0
groot60=0

while (i<10):
    getal = random.uniform(1, 100)
    if getal < 30:
        klein30 = klein30+ 1
        i=i+1
    elif (getal >=30 and getal < 60):
        tussen = tussen + 1
        i = i + 1
    elif (getal >= 60):
        groot60= groot60+1
        i = i + 1

print(f'Er zijn {klein30} getallen kleiner dan 30')
print(f'Er zijn {tussen} getallen tussen 30 en 60')
print(f'en er zijn {groot60} getallen groter dan 60')

"""



# Schrijf een programma waarin er 10 sommen gevraagd worden de gebruiker lost deze op door invoer,
# uiteindelijk geef je een score van 1 tot 10.
import random

i=0
getaleen = 0
getaltwee = 0
score = 0
fouten = 0

while (i<3):
    getaleen = int(random.uniform(1,100))
    getaltwee = int(random.uniform(1,100))
    uitkomst= int(input(f'Wat is de som van {getaleen} + {getaltwee} = '))
    oplossing = getaleen + getaltwee
    i=i+1
    if (oplossing == uitkomst):
        score = score +1
    else:
        fouten = fouten + 1

if (fouten == 1):
    print(f'Uw score is {score}, u heeft {fouten} som fout beantwoord')
else:
    print(f'Uw score is {score}, u heeft {fouten} sommen fout beantwoord')
