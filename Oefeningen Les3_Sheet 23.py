# Schrijf een programma dat feedback geeft op je BMI. Houd het positief

"""gewicht = float(input('Wat is uw gewicht?'))
lengte = float(input('Wat is uw lengte?'))

BMI = gewicht/(lengte**2)

if BMI>25:
    print('Je moet gaan sporten')
else:
    print('Je bent mooi op gewicht')"""

# Schrijf een programma dat de kostprijs berekent voor een pretpark.
# Onder de 10 jaar gratis.
# Tussen 10 en 13: 10 euro
# Studenten 13 jaar en 22 jaar: 15 euro
# Volwassen: 18 euro
# Mensen met abonnement krijgen 10 % korting.


"""prijs1013 = 10
prijsstudent = 15
prijsvolwassenen = 18

leeftijd= int(input('Wilt u de prijs van een ticket berekenen geef dan aub uw leeftijd in '))
if leeftijd<10:
    print('Jouw ticket is gratis')
else:
    abonnement = str(input('Heeft u een abonnement, antwoord aub met Ja of Nee '))
    if abonnement.lower() == 'ja':
        korting = 0.9
    else:
        korting = 1

if leeftijd < 13:
    print(f'Jouw ticketprijs is {prijs1013*korting}')

elif leeftijd <= 22 or leeftijd >= 18:
    student= str(input('Studeer jij, antwoord aub met Ja of Nee '))
    if student.lower() == 'ja' and leeftijd <= 22:
        print(f'Jouw ticketprijs is {prijsstudent*korting}')
    elif student.lower() == 'nee' and leeftijd <= 18:
        print(f'Jouw ticketprijs is {prijsstudent * korting}')
    elif leeftijd >= 18:
        print(f'Jouw ticketprijs is {prijsvolwassenen * korting}')"""




