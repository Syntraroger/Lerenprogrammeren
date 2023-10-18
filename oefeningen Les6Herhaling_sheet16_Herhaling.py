# Een klinkerwerker legt op 1 uur, 12 m², zijn uurtarief bedraag 40 euro per uur btw in.
# Er zijn 3 maten in klinker
# 10x10 cm: 14euro per m²
# 12x12 cm: 16euro per m²
# 14x14 cm 16,5euro per m²
# Indien er oude klinker of kiezels verwijdert moeten worden telt hij het uur prijs,
# hij verwijderd 15m² per uur.
# Voor het vervoer vraag hij 5 euro + 0,30 cent per km boven de 10 km.
# De werkuren worden samengeteld indien hij legt en verwijderd. Werkuren worden altijd naar boven afgerond.
import math
uurtarief = 40
M2peruur = 12
tien = 14
twaalf = 16
veertien = 16,5
M2verwuur = 15
vervoer_perkm = 5
vervoer_bov10km = 5.3

m2= int(input('Hoeveel m2 moet er gelegd worden? '))
verwijderen= int(input('Hoeveel m2 klinkers moeten er verwijderd worden? '))
kmtotwerk= int(input('Geef de km tot het werk aan? '))
selecteerklinkers= int(input('Welke klinkers 1.10x10 2.12x12  3.14x14 '))

prijsklinkersleggen = m2/12 * uurtarief
print(prijsklinkersleggen)
if selecteerklinkers == 1:
    prijsklinkers = m2 * 14
    print(prijsklinkers)
elif selecteerklinkers ==2:
    prijsklinkers = m2 * 16
    print(prijsklinkers)
elif selecteerklinkers == 3:
    prijsklinkersleggen = m2 * 16
    print(prijsklinkers)
else:
    print('er is geen klinker geslecteerd')

prijsverwijderen = (m2/15)*uurtarief
print(prijsverwijderen)

if kmtotwerk > 10:
    prijsafstand = kmtotwerk * 5,3 - 3
    print(prijsafstand)
else:
    prijsafstand = kmtotwerk * 5
    print(prijsafstand)
totaal = math.ceil(prijsverwijderen+prijsklinkers+prijsafstand+prijsklinkersleggen)

print(totaal)
