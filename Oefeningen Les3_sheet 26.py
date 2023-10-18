# Volgens de mobiliteit verplaats je je best
# < 2 km te voet
# < 10 km met de fiets
# > 10 km indien je over een wagen beschikt, anders het openbaar vervoer.

afstand = float(input('Hoeveel KM wil je afleggen '))

if afstand < 2:
    print('Dit kan het beste te voet')
elif afstand <= 10:
    print('Dit kan het beste per fiets')
elif afstand >10:
    print('Dit kan het beste met uw auto of per openbaar vervoer')