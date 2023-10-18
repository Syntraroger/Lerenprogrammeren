# Schrijf een programma dat  bepaald of een woord lang of kort is
# Minder dan 4 letters: heel kort
# Tussen 4 en 6 letters: kort
# Tussen 6 en 10 letter: gemiddeld
# Meer dan 10: Lang

"""woord = str(input('Geef een woord in om de lengte te bepalen '))

if len(woord) < 4:
    print('Dit is een heel kort woord')
elif    len(woord) >= 4 and len(woord) <=6:
    print('Dit is een kort woord')
elif    len(woord) >6 and len(woord)<=10:
    print('Dit is een gemiddeld woord')
elif    len(woord) > 10:"""

# Schrijf een programma dat zegt of een hoek, stomp scherp of recht is.

"""hoek= int(input('Geef het aantal graden van een hoek aan '))

if hoek > 180 and hoek <360:
    hoek = hoek -180

if hoek == 90:
    print('Dit is een rechte hoek')
elif hoek < 90:
    print('Dit is een scherpe hoek')
elif hoek > 90 and hoek <180:
    print('Dit is een stompe hoek')
elif hoek == 180:
    print('Dit is een gestrekte hoek')
elif hoek == 360:
    print('Dit is een volle hoek')"""

# Schrijf een programma waar de punten van 5 vakken ingegeven worden.
# Is het gemiddelde lager dan een 3: zware onvoldoende. <5 onvoldoende, < 7 voldoende.
# 8 = goed, 9 = heel goed, 10 is prima

"""
engels = int(input('Geef punt voor Engels in '))
duits = int(input('Geef punt voor Duits in '))
frans = int(input('Geef punt voor Frans in '))
wiskunde = int(input('Geef punt voor Wiskunde in '))
natuurkunde = int(input('Geef punt voor Natuurkunde in '))

totaal = (engels+duits+frans+wiskunde+natuurkunde) /5

if totaal <= 3:
    print('Het gemiddelde is zwaar onvoldoende')
elif totaal < 5:
    print('Het gemiddelde is onvoldoende')
elif totaal < 8:
    print('Het gemiddelde is voldoende')
elif totaal < 9:
    print('Het gemiddelde is goed')
elif totaal < 10:
    print('Het gemiddelde is heel goed')
elif totaal == 10:
    print('Het gemiddelde is prima')"""