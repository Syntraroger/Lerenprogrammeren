import math

form = input("give the form of the swimming pool: \n S = square \n R = rectangular \n C = circle")
material = input("chose the material \n S = steel \n W = Wood ")
priceM2, priceCm, formL, formH, Cr_Rad, M2, M3 = 0, 0, 0, 0, 0, 0, 0
height = int(input("what is the height of the poo?"))

# the squre meters price per material
if form.upper() == "S":
    Sqside = int(input("give me one side of the pool "))
    M2 = Sqside ** 2
elif form.upper() == "R":
    formL = int(input("give me the length of the pool "))
    formH = int(input("give me the breed of the pool "))
    M2 = formH * formL
elif form.upper() == "C":
    Cr_Rad = int(input("give me the radius of the circle "))
    M2 = (2 * math.pi) * Cr_Rad
print("the M2 are ", round(M2))

if material.upper() == "S":
    priceM2 = M2 * 115
elif material.upper() == "W":
    priceM2 = M2 * 100
print("the price for the materials is: ", priceM2)

priceCm = priceM2 * (height - 150) * 0.02
print("the extra is: ", priceCm)
M3 = M2 * height / 100
digcost = M3 * 60
print("the digging cost is: ", digcost)
if M3 <= 50:
    priceWork = M3 * 20
elif M3 <= 100:
    priceWork = M3 * 18
else:
    priceWork = M3 * 15
print("The work costs are: ", priceWork)
Total_price = priceM2 + priceWork + priceCm + digcost
print(Total_price)