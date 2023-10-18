# Schrijf een programma dat controleert of een getal deelbaar is door 2,3,5,7.

"""priemgetal = int(input('Geef een getal in '))
x=2
y=1
z=0

while(x < 8):
    if (priemgetal%x == 0):

        print(f'Het getal is deelbaar door {x}')
        x = x + y   # volgend priemgetal bepalen namelijk 3
        y=2         # volgend priemgetal bepalen namelijk 5 en 7
        z=1         # Status bepalen om na te gaan of het ingegeven getal een priemgetal is
    else:
        x=x+y
        y=2

if (z==0):
    print('Niet deelbaar het ingegeven getal is een priemgetal')
"""
# """if (priemgetal%x == 0):
#     print('Het getal is deelbaar door 2')
#     x=x+1
# else:
#     x=x+1"""
# """elif (priemgetal%3 ==0):
#     print('Het getal is deelbaar door 3')
# elif (priemgetal%5 ==0):
#     print('Het getal is deelbaar door 5')
# elif (priemgetal%7 == 0):
#     print('Het getal is deelbaar door 7')
# else:
#     print('Het getal is niet deelbaar door 2, 3, 5 of 7')
# """


# Schrijf een programma dat vereenvoudigd in priemgetallen.

getal= int(input('Geef een geheel getal in: '))
twee=0
drie=0
vijf=0
zeven=0


while (not getal==0):
    if (getal==1):
        getal = 0
        break
    if(getal%2==0):
        twee=twee+1
        getal = getal/2
    elif(getal%3==0):
        drie=drie+1
        getal = getal / 3
    elif(getal%5==0):
        vijf=vijf+1
        getal = getal / 5
    elif(getal%7==0):
        zeven=zeven+1
        getal = getal / 7
    else:
        print(f'De restwaarde is een priemgetal {getal}')
        break

print(f'Het getal is kan vereenvoudigd worden met {twee} *2, met {drie} *3, met {vijf} *5, met {zeven} * 7, en de rest is {getal}')