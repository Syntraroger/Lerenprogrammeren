# Een schrijnwerker geeft figuren in tot de invoer “stop” is.
# Hij kan kiezen uit volgende oppervlaktes
# Vierkant
# Rechthoek
# Driehoek
# Cirkel
# Op het einde van het programma wordt er de totale oppervlakte weergegeven.

def figuren ():
    vierkant = 0
    rechthoek = 0
    driehoek = 0
    cirkel = 0
    opp = 0
    invoer = ''
    while (not invoer == 'stop'):
        invoer = input('Geef een figuur in 1.Vierkant 2.Rechthoek 3.Driehoek 4.Cirkel of geef stop in stop ')
        if (invoer == '1'):
            vierkant= vierkant + 1
            zijde_vierk = int(input('Geef de zijde van het vierkant in cm '))
            opp= opp + (zijde_vierk**2)
            print(opp)
        elif (invoer == '2'):
            rechthoek = rechthoek + 1
            zijde_rechth = int(input('Geef de lange zijde van de rechthoek in cm '))
            zijde_rechth2 = int(input('Geef de korte zijde van de rechthoek in cm '))
            opp = opp +(zijde_rechth*zijde_rechth2)
        elif (invoer == '3'):
            driehoek = driehoek + 1
            basis = int(input('geef de basis van de driehoek in cm '))
            hoogte = int(input('geef de hoogte van de driehoek in cm '))
            opp = opp + ((basis * hoogte) /2)
        elif (invoer == '4'):
            cirkel = cirkel + 1
            dia = int(input('geef de diameter van de cirkel in cm '))
            opp = opp + ((3.14 * dia**2)/4)

    print("De totale oppervlakte is:", opp)

figuren()


