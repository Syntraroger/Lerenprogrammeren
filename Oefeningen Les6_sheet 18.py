# Maak een functie tekenvierkant(z,teken)
# Bvb tekenvierkant(3,”*”)
# * * *
# * * *
# * * *


"""
def tekenvierkant(z,teken):
    hori=''
    for i in range(z):
        for i in range(z):
            hori = hori + teken
        print(hori)
        hori =''



tekenvierkant(3, '*')"""

# Schrijf een functie split getallen, naar D H T E. bvb 1234
# 1D + 2H +3T+ 4E
"""
def split(getal):
    D = 0
    H = 0
    T = 0
    E = 0
    while not (getal == 0):
        if getal > 1000:
            getal = getal - 1000
            D += 1

        elif getal >= 100:
            getal = getal - 100
            H += 1
        elif getal >= 10:
            getal = getal - 10
            T += 1
        elif getal >= 1:
            getal = getal -1
            E += 1

    print(f'{D} Duizendtallen, {H} Honderdtallen, {T} Tientallen, {E} eenheden')

split(100)"""


# -----------------------------------------------------------------------------------------------------------------------------------------
# Schrijf een functie split getallen, naar D H T E. bvb 1234
# 1D + 2H +3T+ 4E
# -----------------------------------------------------------------------------------------------------------------------------------------
def split():
    getal = (input("Geef een getal <10000: "))
    list1 = list(getal)
    list1.reverse()
    list2 = ["E", "T", "H", "D"]
    list_comb = []
    for i in range(0, len(list1)):
        list_comb.append(list1[i] + list2[i])
    list_comb.reverse()                                 #Anders probleem met hondertallen daarom reverse
    return list_comb


list1 = split()
for i in list1:
    print(i, end=" ")