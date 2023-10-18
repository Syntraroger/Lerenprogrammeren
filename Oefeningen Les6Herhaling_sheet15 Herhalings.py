"""
Casus 1

prijs                   extra                   Korting
<12 jaar: 4 euro        Langspeelfilm + 2 euro  Studentenkaart < 25 jaar - 2 euro
<18 jaar: 5 euro        3D film + 2 euro
>18 jaar: 6 euro

Vraag aan de gebruiker hoeveel personen druk daarna per persoon de prijs af en de totaalprijs.

"""

def prijs_per_pers ():
    pers=int(input('Hoeveel personen gaan naar de film: '))
    film=int(input('1.standaard, 2.lange Speelfilm 3.3D Film '))
    totaal = 0

    for i in range(pers):
        leeftijd=int(input(f'Hoe oud is persoon {i+1} '))

        if leeftijd < 12:
           totaal = totaal + 4

        elif leeftijd < 18:
            stukaart = input('Heb je een studentenkaart: ')
            if stukaart == 'ja':
                totaal = totaal + 5 - 2
            else:
                totaal = totaal + 5
        elif leeftijd >= 18:
            if leeftijd <25:
                stukaart = input('Heb je een studentenkaart: ')
                if stukaart == 'ja':
                    totaal = totaal + 6 - 2
                else:
                    totaal = totaal + 6
            else:
                totaal = totaal+6
    if film == 3 or film == 2:
        totaal = totaal + pers*2

    print(f'De prijs voor alle personen is {totaal} ')

prijs_per_pers()