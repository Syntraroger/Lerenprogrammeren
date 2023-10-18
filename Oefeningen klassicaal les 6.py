
"""

def steden():
    steden = ['Berlijn', 'Brussel', 'Maastricht', 'Parijs']
    totaal = 0

    for stad in steden:
        totaal += len(stad)

    print(totaal)

steden()"""


"""lijst =[]

lengte = int(input('Hoe veel namen wilt u ingeven '))

for i in range(0,lengte):
    naam = input('Geef de naam in ')
    lijst.append(naam)

print(lijst)

for naam in lijst:
    print(naam)"""

def maak_lijst_namen(aantal):
    lst = []
    for n in range(aantal):
        naam= input('geef de naam in ')
        lst.append(naam)

    return lst
    # for item in lst:
    #     print(item)

# namen = maak_lijst_namen(3)
#
# for naam in namen:
#     print(naam)"""


