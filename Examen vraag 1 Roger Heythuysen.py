import random

# Casus 1: Willekeurige lijst.
# · Vul een lijst met 47 willekeurige getallen tussen 20 en 200.
# · De gebruiker geef hierna zelf nog 3 getallen in. Geen invoercontrole nodig
# · Druk de 3 grootste getallen uit de lijst af
# · Toon het gemiddelde van de lijst.
# · Druk de lijst van groot naar klein af.

i=0
lijst=[]
som = 0
while i < 47:

    lijst.append(round(random.uniform(20,199),0))

    som = som + lijst[i]
    i += 1
print(lijst)
for i in range(3):
    lijst.append(int(input(f'Geef gatal {i+1} van 3 in ')))
lijst.sort()

for i in range(48,50):
    print(lijst[i])

print(len(lijst))
print('De gemiddelde waarde =', som/50)



for i in range(50):
    print(lijst[49-i])
print(lijst)