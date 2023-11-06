# Casus 2: Aanspreking met gebruik van een functie, afdruk gebruik vanuit de functie
# De gebruiker geeft 3 keer de waarde van de functie in
# · Aanspreking(geslacht,Familie_naam,beroep)
# · Indien het geslacht M: Heer, Geslacht V: Mevrouw
# · Titel, deze titels zijn gekend door het programma.
#       o Dokter: Dr.
#       o Professor: Prof.
#       o Ingenieur: Ir.
#       o Andere: Geen ansprekeing
#            § Titels worden niet gecombineerd in deze opdracht.
# · Voorbeeld output(Man,Peeters,Dokter): Geachte Heer Prof Peeters.


def aanspreking(geslacht,Familie_naam,beroep):
    if geslacht.lower()== 'm' and beroep == 1:
        print('Geachte heer Dr.', Familie_naam)
    elif geslacht.lower()== 'v' and beroep == 1:
        print('Geachte mevrouw Dr.', Familie_naam)
    elif geslacht.lower()== 'm' and beroep == 2:
        print('Geachte heer Prof.', Familie_naam)
    elif geslacht.lower()== 'v' and beroep == 2:
        print('Geachte mevrouw Prof.', Familie_naam)
    elif geslacht.lower()== 'm' and beroep == 3:
        print('Geachte heer Ir.', Familie_naam)
    elif geslacht.lower()== 'v' and beroep == 3:
        print('Geachte mevrouw Ir.', Familie_naam)
    elif geslacht.lower()== 'm' and beroep == 4:
        print('Geachte heer ', Familie_naam)
    elif geslacht.lower()== 'v' and beroep == 4:
        print('Geachte mevrouw ', Familie_naam)


for i in range(3):
    gesl = input('wat is het geslacht M: heer of V: Mevrouw ')
    naam = input('Geef uw familie naam op ')
    beroep = int(input('Geef uw beroep 1.Dokter, 2.Professor, 3.Ingenieur, 4.Geen Titel '))
    aanspreking(gesl, naam, beroep)
