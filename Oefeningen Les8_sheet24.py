# Vertaal naar waarde tabel. Zet daarna de logica om in code.
# Een leerling legt 3 proeven af. Een leerling kan enkel slagen onder volgende voorwaarde.
# Alle proeven gaan op 10 punten
# Is geslaagd voor alle proeven(5 of meer)   678
# Heeft 9of10 op proef 1 en geslaagd op proef 2 of 3   kan zaken op een proef 9 7 2
# Heeft een gemiddelde van 7 op 10 op alle 3 proeven. kan zakenop een proef 10 8 3


gem = 0
puntenlijst = []
for i in range(3):
    puntenlijst.append(input(f'Geef een cijfer voor proef {i+1} in '))
    gem = gem + int(puntenlijst[i])


if int(puntenlijst[0])>=9 and int(puntenlijst[1])>=5 or int(puntenlijst[i])>=5:
    print('geslaagd')
elif int(puntenlijst[0])>=5 and int(puntenlijst[1])>=5 and int(puntenlijst[i])>=5:
    print('geslaagd')
elif gem >= 21:
    print('geslaagd')
else:
    print('gezakt')