# Schrijf een programma dat alle vermenigvuldigen van een ingegeven getal geeft dat kleiner is dan 1000.

"""getal=int(input('Geef een getal in '))
verm= 0
i = 1
while verm < 1000:

     verm = i * getal
     i += 1

     if verm >= 1000:
         break
     print(verm)"""


# Pas het programma aan dat je een eindgetal ingeeft.
# Geef een melding als het eindpunt kleiner is dan het vermenigvuldig getal.

getal=int(input('Geef een getal in '))
einde=int(input('Geef het eindgetal in '))

if einde<getal:
    print('Het eind getal is kleiner dan het verminigvuldigen getal')
    einde=int(input('Geef het eindgetal in '))
verm= 0
i = 1
while verm < einde:

     verm = i * getal
     i += 1

     if verm >= einde:
         break
     print(verm)



# Schrijf een programma dat je naam spelt.

"""naam = str(input('Geef je voornaam in '))

for i in range(len(naam)):
    print(naam[i])
"""



