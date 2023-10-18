"""getal = int(input('Geef een getal in : '))

if (getal > 10 and getal < 100):       #Gebruik de and om er voor te zorgen dat de opgegeven range klopt
    print(f'Het getal ligt tussen 10 en 100 en is {getal}')
else:
    print('het getal ligt buiten de opgegeven range')"""

#-----------------------------------------------------
"""getal = int(input('Geef een getal in :'))
tem = int(input("geef het bereik in"))

for maaltafel in range(1, tem+1,2):   # stappen van 2
        print(maaltafel, maaltafel*getal)
"""
"""for i in range(1,11):
    print(getal, '*', i,'is', getal*i)"""
# -------------------------------------------------
"""tekst= ('Dit is een regel')
for teken in tekst:
    print(teken)"""
# --------------------------------
"""for i in range (1,105):
    if i==55:
        print('einde')
        break
    print("test",i)"""
#---------------------------------

"""bereik = range (10,1000,15)
for i in bereik:
    print(i)"""


# ------------------------
begin= int(input("start " ))
einde = int(input("stop "))

while einde<begin:
    einde = int(input(f'Geef een getal dat groter is dan begin {begin}'))

stap = int(input("stap "))
bereik = range (begin, einde, stap)
for i in bereik:
    print(i)

