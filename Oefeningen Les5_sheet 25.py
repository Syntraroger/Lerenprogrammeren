# Maak een functie tekenvierkant(z,teken)
# Bvb tekenvierkant(3,”*”)
# * * *
# * * *
# * * *

def tekenvierkant(z, teken):

    lijs=''

    for i in range(z):
        for i in range(z):
            lijs= lijs+teken
        print(lijs)
        lijs=''


tekenvierkant(4,'*')

