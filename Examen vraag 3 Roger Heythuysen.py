aantl = int(input('Hoeveel fietsen wenst u te huren? '))

def verzekering(soort, dagen):
    prijs = 0
    if soort == 1:
        prijs = 8*dagen
    elif soort == 2 or soort == 3:
        prijs = 10 * dagen
    elif soort == 4:
        prijs = 15 * dagen
    elif soort == 5:
        prijs = 25 * dagen
    return prijs

def kostprijs(aantal):
    som = 0
    dagen = 0
    lijst=[]
    for i in range(aantal):

        soort=input('Welke type fiets wilt u huren 1.kinderfiets, 2.Volwassenfiets, 3.tandem, 4. ElectrischeFiets of 5.Pedelec')
        dagen = int(input('Hoeveel dagen wilt u deze fiets huren? '))
        verz = input('wilt u deze fiets verzekeren ja of nee ')
        if soort == '1' :
            som = som + (30*dagen) + 100
            if verz == 'ja':
                som = som + verzekering(1,dagen)
        elif soort == '2':
            som = som + (40*dagen) + 150
            if verz == 'ja':
                som = som + verzekering(2,dagen)
        elif soort == '3':
            som = som + (50*dagen) + 150
            if verz == 'ja':
                som = som + verzekering(3,dagen)
        elif soort == '4':
            som = som + (50*dagen) + 200
            if verz == 'ja':
                som = som + verzekering(4,dagen)
        elif soort == '5':
            rijb = input('Heeft u een rijbewijs ja of nee ')
            if rijb.lower() == 'ja':
                som = som + (70*dagen) + 350
                if verz == 'ja' and soort == '5':
                    som = som + verzekering(5, dagen)
            elif rijb.lower() == 'nee':
                print('Omdat u geen rijbewijs heeft krijgt u een electrische fiets')
                som = som + (50*dagen) + 200
                if verz == 'ja' and soort == '4':
                    som = som + verzekering(4, dagen)
        lijst.append(som)
        som = 0
    return lijst


totaal=[]
totaal = kostprijs(aantl)

for i in range(len(totaal)):
    print(f'De totaal prijs van fiets {i+1} is' , totaal[i])