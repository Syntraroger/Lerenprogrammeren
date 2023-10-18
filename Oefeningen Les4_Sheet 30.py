# Schrijf een programma dat alle even getallen tot 256 geeft, startend bij 2.

import random
"""
getal=2

while getal < 256:
    print(getal)
    getal= getal + 2"""

# Schrijf een programma dat het dubbel van een ingegeven getal geeft tot 1000.

"""getal= int(input('Geef een geheel getal kleiner dan 1000 '))

while getal<1000:
    getal= getal*2
    if(getal >1000):
        break
    else:
        print(getal)"""

# Schrijf een programma dat het gemiddelde geeft van alle ingevoerde getallen , de invoer stopt bij stop, pas invoercontrole toe.
"""
invoer = ('')
gem = 0
i=0
while(not invoer == 'stop'):
    invoer = input('Geef een getal in of stop ')
    if(invoer == 'stop'):
        break
    else:
        try:
            invoer = int(invoer)
            gem = gem + invoer
            i= int(i+1)
        except ValueError:
            print("gelieve een geheel getal in the geven ")

print("Het gemiddelde is: ",gem/i)"""

# Schrijf een programma dat onthoud hoeveel even en oneven getallen de gebruiker invoert
# de invoer stopt bij “einde”, pas ook invoercontrole toe.

invoer = ('')
gem = 0
i=0
aantal_evengetallen=0
aantal_onevegetallen=0

while(not invoer == 'einde'):
    invoer = input('Geef een getal in of stop door het woord einde in te voeren ')
    if(invoer == 'einde'):
        break
    else:
        try:
            invoer= int(invoer)
            if (invoer%2==0):
                aantal_evengetallen = aantal_evengetallen+1
            else:
                aantal_onevegetallen = aantal_onevegetallen+1
        except ValueError:
            print("gelieve een geheel getal in the geven ")
        except

print(f"Het aantal evengetallen is {aantal_evengetallen} en het aantal onevengetallen is {aantal_onevegetallen}")