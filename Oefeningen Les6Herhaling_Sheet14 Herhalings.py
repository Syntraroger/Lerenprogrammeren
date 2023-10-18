# Schrijf een programma dat Britse pond omzet naar us dollar
"""bedrag = int(input('Geef het bedrag op dat u wilt omzetten naar dollars'))

pond=1.78

dollar=int(pond*bedrag)

print(dollar)"""


# Schrijf een programma dat berekent hoeveel liter water in een cilindervormig zwembad kan.

"""diameter= float(input('Geef de diameter van het zwembad op : '))
hoogte= float(input('Geef de hoogte van het zwembad op : '))


inhoud= print(round(((3.14*(diameter/2)**2)*hoogte),2))
"""


# Breid het programma van de munteenheden uit.
# De gebruiker kan kiezen om Britse pond om te zetten naar
# 1, euro. 2, dollar, 3 yen, 4 munteenheid naar keuze.

"""bedrag = int(input('Geef het bedrag op dat u wilt omzetten'))
munteenheid = int(input('Geef de munt eenheid 1 = euro, 2 = dollar, 3 = yen, 4 = Sloty'))

dollar= 1.7
euro= 1.5
yen=2
sloty=4

if munteenheid ==1:
    print(f'Dit zijn {euro*bedrag} euros')
elif munteenheid ==2:
    print(f'Dit zijn {dollar * bedrag} dollars')
elif munteenheid ==3:
    print(f'Dit zijn {yen * bedrag} yen')
elif munteenheid ==4:
    print(f'Dit zijn {sloty * bedrag} sloties')
else:
    print('U heeft een foutieve munteenheid ingegeven')

"""

# Schrijf een programma om te controleren of een getal deelbaar is door 3
"""
getal= int(input('Geef een geheel getal in: '))

if getal%2==0:
    print('Het getal is deelbaar door 2, ingevoerd getal:', getal)
else:
    print('Het getal is niet deelbaar door 2')"""
# Maak een programma dat telt hoeveel keer een getal deelbaar is door 2

"""getal= int(input('Geef een geheel getal in : '))
x=0
while getal%2 ==0:
    getal = getal / 2
    x =+ 1

print(f'Het getal is {x} maal deelbaar door 2')"""


# Schrijf een programma dat alle priemgetallen tot 100 weergeeft gebruik de zeef van eratosthenes

def SieveOfEratosthenes(num):
    prime = [True for i in range(num + 1)]  #Adding TRUE to every position in the list with a length of parameter NUM
    #[roger] print(prime)
    # boolean array
    p = 2
    while (p * p <= num): #Zolang that het kwadraat van p kleiner of gelijk aan hoogste waarde in de lijst

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True): #kijk of de locatie van index p waar is, zo ja voer if statement uit

            # Updating all multiples of p naar FALSE zodat deze uiteindelijk allen de priem getallen op true blijven staan
            for i in range(p * p, num + 1, p):  # p*p = het getal dat false moet worden, num is de range, p is de stap
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, num + 1):
        if prime[p]:
            print(p)

SieveOfEratosthenes(100)
