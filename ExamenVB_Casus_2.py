# Gebruiker kiest een categorie: A: Ford Fiesta, B: Ford Focus, C: Ford Puma, D: Ford Kuga
# Prijs per dag A: 55 euro, B: 70 euro, C: 80 euro, D: 90 euro.
# Prijs per KM gereden: 0,18 euro 20 km gratis. C en D  hebben 50 km gratis.
# Dus cat B 2 dagen en 40 km is: 2*70+(40-20)*0,18.
#
# All-in pakket met verzekering: A en B + 25 euro per dag, C en D + 40 euro per dag.
# 	+ 100 km gratis(Voor alle categorieën) in totaal(dus niet per dag)
#
# De gebruiker simuleert 3 autos: Zet de totaalprijzen in een lijst. Druk ze vervolgens regel per regel af met optie 1,2,3
# Vb Afdruk: Optie 1: x euro in totaal.




prijsa=55
prijsb=70
prijsc=80
prijsd=90
kmprijs=0.18
gratisAB=20
gratisCD=50
verzAB=25
verzCD=40
verzkm=100
aantalkm=0
aantaldagen=0
lijst=[]


def tot(auto, dagen, km, allin):
    totaal = 0

    if auto.lower() == 'a':
        totaal = dagen * prijsa
        if allin == 'ja':
            totaal += (km-100-gratisAB) * kmprijs
        else:
            totaal += (km-gratisAB) * kmprijs
        return totaal
    elif auto.lower() == 'b':
        totaal = dagen * prijsb
        if allin == 'ja':
            totaal += (km - 100 - gratisAB) * kmprijs
        else:
            totaal += (km - gratisAB) * kmprijs
        return totaal
    elif auto.lower() == 'c':
        totaal = dagen * prijsc
        if allin == 'ja':
            totaal += (km - 100 - gratisCD) * kmprijs
        else:
            totaal += (km - gratisCD) * kmprijs
        return totaal
    elif auto.lower() == 'd':
        totaal = dagen * prijsd
        if allin == 'ja':
            totaal += (km - 100 - gratisCD) * kmprijs
        else:
            totaal += (km - gratisCD) * kmprijs
        return totaal


for a in range(3):
    sel = input('A:Ford Fiesta, B:Ford Focus, C:Ford Puma, D:Ford Kuga: ')
    aantaldagen = int(input('Hoeveel dagen wilt u de auto huren: '))
    aantalkm = int(input('Hoeveel km verwacht u nodig te hebben: '))
    Allin = input('Wilt u een All-in verzekerings pakket ja/nee: ')

    lijst.append(tot(sel, aantaldagen, aantalkm, Allin))



for b in range(3):
    print(f'Optie {b+1}: ', lijst[b], 'euro in totaal')




# if sel.lower() == 'a' and Allin.lower()=='ja':
    #         lijst.append(tot(sel, aantaldagen, aantalkm, Allin))
    # elif sel.lower() == 'a' and Allin.lower()=='nee':
    #         lijst.append(tot(sel, aantaldagen, aantalkm, Allin))
    # elif sel.lower() == 'b' and Allin.lower()=='ja':
    #         lijst.append(tot(sel, aantaldagen, aantalkm, Allin))
    # elif sel.lower() == 'b' and Allin.lower()=='nee':
    #         lijst.append(tot(sel, aantaldagen, aantalkm, Allin))
    # elif sel.lower() == 'c' and Allin.lower()=='ja':
    #         lijst.append(tot(sel, aantaldagen, aantalkm, Allin))
    # elif sel.lower() == 'c' and Allin.lower()=='nee':
    #         lijst.append(tot(sel, aantaldagen, aantalkm, Allin))
    # elif sel.lower() == 'd' and Allin.lower()=='ja':
    #         lijst.append(tot(sel, aantaldagen, aantalkm, Allin))
    # elif sel.lower() == 'd' and Allin.lower()=='nee':
    #         lijst.append(tot(sel, aantaldagen, aantalkm, Allin))


