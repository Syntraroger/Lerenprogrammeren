deelnemers = int(input('Geef het aantal deelnemers in: '))


lijst=[]
tijd=0

for i in range(deelnemers):
    looptijd = int(input('Geef de looptijd in minuten in: '))
    lijst.append(looptijd)
    tijd += looptijd

lijst.sort()
print('De gemiddelde looptijd is: ', round(tijd /deelnemers, 2))
aantal = deelnemers - 1

for i in range(3):
    # print 3 snelste tijden
    print(lijst[i])


    # laatste 3 printen, langzaamste
    # print(lijst[aantal])
    # aantal = aantal - 1
