# Een schilder vraagt 35 euro per uur ex btw,
# Hij schildert 18m² op 1 uur, dit is 1 laag.
# Het programma vraagt het aantal muren.
# De verf kost 15 euro per liter ex btw. 1 liter is 22m²
#
# Bereken de kostprijs incl btw. Gebruik functies.
# Oudhuis <1980 6% erna is 21% btw

def oppervlakte_berekenen (aantal_muren):
    totaal = 0
    for i in range (aantal_muren):
        opp=int(input(f'Wat is de oppervlakte van muur {i +1}: '))
        totaal = totaal + opp
        lagen=int(input(f'Hoeveel lagen moeten er worden aangebracht op muur {i+1}: '))
        totaal = totaal * lagen
    prijs_uur = int(totaal/18 * 35)
    print(prijs_uur)
    prijs_verf= int(totaal/22*15)
    print(prijs_verf)
    prijs_totaal = prijs_verf+prijs_uur
    print(prijs_totaal)
    kostprijs_btw(prijs_totaal)


def kostprijs_btw(kost):
    leeftijd_woning = int(input('Wat is het bouwjaar van de woning? '))

    if leeftijd_woning<1980:
        btw=kost*1.06
    else:
        btw=kost*1.21

    print(btw)





aantal_muren = int(input('Hoeveel muren wil je gaan verven? '))

oppervlakte_berekenen(aantal_muren)