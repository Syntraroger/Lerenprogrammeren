"""hoa = input('(H)uis of (A)ppartement ')
opp = int(input('Wat is de oppervlakte van de woning '))
Leeftijd= int(input('Wat is de leeftijd van de woning '))

if (hoa == 'H') and (opp>200 or Leeftijd>20):
    print('U moet belasting betalen ')
elif (hoa == 'A') and Leeftijd>50:
    print('U moet belasting betalen ')
else:
    print('Geen belasting betalen ')
"""


"""
x=0
y=0

def gevordered(x):
    for i in range(x):
        gesl = input('(M)an of (V) ')
        L = int(input('km lopen? '))
        Z = int(input('km zwemmen? '))
        F = int(input('km fietsen? '))
        if gesl == 'M' and L > 15 and Z > 3 and F > 40:
            print('gevorderde groep')
            x =+ 1
        elif gesl == 'V' and L > 12 and Z > 2 and F > 30:
            print('Gevorderde groep')
            y =+1

    print(f'Er zijn {x} mannen die gevorderd zijn en er zijn {y} vrouwen die gevorderd zijn')


gevordered(5)"""

aantal_personen = int(input("geef het aantal personen in"))
list_resultaten = []
for i in range(aantal_personen):
    naam = input("geef naam")
    geslacht = input("m of v")
    lopen = float(input("geef het aantal m lopen"))
    zwemmen = float(input("geef het aantal m zwemmen"))
    fietsen = int(input("geef het aantal km fietsen"))
    if geslacht == "m" and lopen > 20000 and zwemmen > 5000 and fietsen > 80:
        list_resultaten.append(str(naam + " Proficiat u bent Experte"))
    elif geslacht == "v" and lopen > 15000 and zwemmen > 4000 and fietsen > 70:
        list_resultaten.append(str(naam + " Proficiat u bent Expert"))
    elif geslacht == "m" and lopen > 15000 and zwemmen > 3000 and fietsen > 40:
        list_resultaten.append(str(naam + " Proficiat u bent Gevorderde"))
    elif geslacht == "v" and lopen > 12000 and zwemmen > 2000 and fietsen > 30:
        list_resultaten.append(str(naam + " Proficiat u bent Gevorderde"))
    else:
        list_resultaten.append(str(naam + " Nog oefenen"))

for res in list_resultaten:
    print(res)