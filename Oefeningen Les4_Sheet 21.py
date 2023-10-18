# Tel 2 willekeurige getallen op tussen 100 en 200.
"""import random

getal1= round(random.uniform(100, 200),2)
getal2= round(random.uniform(100, 200),2)


som= getal2+getal1
print(getal1,'+',getal2,'=',som)"""
import random

# Genereer een even willekeurig getal tussen 10 en 30
"""
getal=random.choice(range(10,30, 2))

print(getal)"""

# Controleer of een getal deelbaar is door 2 en ook door 3.
"""getal = int(input("geef een getal in"))
if getal%3==0 and getal%2==0:
    print("het getal is deelbaar door 2 en 3")
else:
    print("het getal is niet deelbaar door 2 of 3")
"""


# Neem grootste getal van 3 willekeurige getallen tussen 1 en 1000

"""a=random.uniform(1,1000)
b=random.uniform(1,1000)
c=random.uniform(1,1000)

print(a)
print(b)
print(c)

if a>b and a>c:
    print('getal a is het grootste', a)
elif b>a and b>c:
    print('getal b is het grootste', b)
else:
    print('getal c is het grootste', c)"""
# Neem het kleinste getal van 3 willekeurige getallen.
a=random.uniform(1,1000)
b=random.uniform(1,1000)
c=random.uniform(1,1000)

print(a)
print(b)
print(c)

if a<b and a<c:
    print('getal a is het kleinste', a)
elif b<a and b<c:
    print('getal b is het kleinste', b)
else:
    print('getal c is het kleinste', c)