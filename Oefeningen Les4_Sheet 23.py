# Een verver zijn uur tarief is 28 euro per uur,
# binnen de tijd brengt hij 1 laag aan van 20 m².
# met 1l verf doet hij 10m².
# hij vraagt 12 euro per liter voor de verf,
# 16 euro per liter als de verf op waterbasis is en ook afwasbaar.

"""
uur_tarief_euro = 28
m2_per_uur= 20
euro_1liter_verf = 12
euro_1leter_afw = 16

m2= int(input('Hoeveel vierkante meter moet er geverfd worden? '))
soort_verf= str(input('wilt u afwasbare verf ja of nee? '))

if soort_verf.lower()=='ja':
    prijs= ((m2/20)*uur_tarief_euro) + ((m2/10)  *euro_1leter_afw)
    print(f'De totale prijs is {prijs}')
else:
    prijs = ((m2/20) * uur_tarief_euro) + ((m2/10) * euro_1liter_verf)
    print(f'De totale prijs is {prijs}')"""

#
# Schrijf een programma om de kost prijs te geven, de gebruiker geeft het aantal m² in, aantal lagen en soort verf
"""
uur_tarief_euro = 28
m2_per_uur= 20
euro_1liter_verf = 12
euro_1leter_afw = 16

m2= int(input('Hoeveel vierkante meter moet er geverfd worden? '))
soort_verf= str(input('wilt u afwasbare verf ja of nee? '))
hoeveel_lagen = int(input('Hoeveel lagen verf wilt u? '))

if soort_verf.lower()=='ja':
    prijs= (((m2/20)*uur_tarief_euro) + ((m2/10)  *euro_1leter_afw) * hoeveel_lagen)
    print(f'De totale prijs is {prijs}')
else:
    prijs = (((m2/20) * uur_tarief_euro) + ((m2/10) * euro_1liter_verf) * hoeveel_lagen)
    print(f'De totale prijs is {prijs}')"""