# Schrijf een programma dat een tafelkaart maakt van alle tafelen tot 20 en 20 keer,
# Tip Geneste for.


# getal=int(input('Geef een getal in '))

"""lijstv = []
for i in range (1,21):
    for x in range (1,21):
        z= i*x
        lijstv.append(z)
    print(lijstv)
    lijstv=[]"""

"""y=''
lijstv = ''
for i in range (1,21):
    for x in range (1,21):
        z= i*x
        if z<10:
            y= '0' + str(z)
            lijstv= lijstv + ' ' + y

        else:
            lijstv= lijstv + ' ' + str(z)
    print(lijstv)
    lijstv=''"""


for i in range (1,21):
    for j in range (1,21):
        print(i*j, end="\t") # end='\t'  dit is een tap
    print("")                # print("") is nieuwe regel,  einde van de print is automatisch een enter


# Schrijf een programma dat alle getallen uit de fibonaccireeks weergeeft tot 200.
#
# 1 1 2 3 5 8 13 21 34
"""
lijsf=[]
x = 1
y = 1
z = 0
lijsf.append(x)
while z < 200:
        z=x+y
        if z>200:
            break
        else:
            x=y
            y=z

        lijsf.append(z)

print(lijsf)"""