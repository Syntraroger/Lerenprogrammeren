# Maak een array met 100 veelvouden van 7.



"""getal = 7
lijst = []
for i in range(100):
    getal = getal + 7
    lijst.append(getal)

print(lijst)"""

# De gebruiker geeft 10 getallen in, maak een array even en oneven waarin ze worden opgeslagen.
"""
even= []
oneven=[]
for i in range(10):
    getal = int(input('Geef een getal in '))
    if getal%2==0:
        even.append(getal)
    else:
        oneven.append(getal)

print(even)
print(oneven)"""



# Maak een array waarin elke letter een ingegeven woord wordt opgeslagen

"""woord = input('Geef een woord ')
lijst = []
a = 0
for i in range (len(woord)):
    lijst.append(woord[i])
    

print(lijst)"""



# Sla 10 getallen op in een array, geef de som van alle waardes.
lijst=[]
som = 0
totaal = 0 
for i in range(10):
    getal = int(input('Geef een getal in '))
    lijst.append(getal)
    totaal = totaal + lijst[i]
# for i in range (len(lijst)):
#     som = som + lijst[i]
som = sum(lijst)
print(lijst)
# print(som)
print(som)



# https://www.geeksforgeeks.org/sum-function-python/