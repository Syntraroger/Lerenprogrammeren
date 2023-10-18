# Kies de vorm van het zwembad: vierkant, rechthoekig, ovaal.
# Kies het Materiaal: Staal of Hout.
# 	Prijs per m²: hout €100, staal €115.
# 	Hoogste standaard: 150 cm, elke centimeter erboven + 2 procent.
# 	Dus zwembad van 200 cm hoogte = basisprijs +50*2 %:
# 	bvb zwembad met 100m² hout van 160 cm hoog
# 		100*100=10000+ (160-150)=10*2% = 20% dus totaalprijs € 12000
# 	Graafwerken € 60 per m³ 10*10*1,6= 160*60 = € 9600
# 	Plaatsingskost:  <= 50 m³= €20 per m³
# 		  <=100m³ = €18 per m³
# 		>100m³ = € 15 per m³
# Druk de kostprijs van het zwembad, de graafkosten en plaatsingskosten en de totaalprijs van het project af.
import math


def oppvierkant(lengte):
    opp = lengte*lengte
    return opp
def inhoudvierkant(lengte, hoogte):
    inh = lengte*lengte*hoogte
    return inh

def opprechthoek(lengte, breedte, ):
    opp = lengte*breedte
    return opp
def inhrechthoek(lengte, breedte, hoogte):
    inh = lengte * breedte * hoogte
    return inh

def oppcirkel(straal):
    opp= (math.pi*straal**2)
    return opp
def inhcirkel(straal, hoogte):
    inh = (math.pi * straal ** 2)*hoogte
    return inh

prijshout = 100
prijsstaal = 150
graafm3 = 60
pltsmin50 = 20
pltsmin100 = 18
pltsplus100 = 15

vorm = int(input(' Wat is de vorm van het zwembad 1.vierkant 2.rechthoek 3 cirkel: '))
materiaal = input('Van welk materiaal moet het zwembad gemaakt worden, hout of staal? ')
hoogte= int(input('Hoe hoog wordt het zwembad? '))

if vorm == 1:
    zijde=int(input('Hoe lang is een zijde '))
    if hoogte <= 150:
        if materiaal.lower() == 'hout':
            prijs = oppvierkant(zijde)*100
        else:
            prijs = oppvierkant(zijde)*115
    elif hoogte>150:
        if materiaal.lower()=='hout':
            extra = (hoogte-150)*0.02
            prijs = oppvierkant(zijde)*100
            prijs += extra*prijs
        else:
            extra = (hoogte - 150) * 0.02
            prijs = oppvierkant(zijde) * 115
            prijs += extra * prijs
    print('de prijs is', prijs)
    prijsgraven = inhoudvierkant(zijde,(hoogte/100))*60
    print('Prijs graafwerkzaamheden zijn', prijsgraven)
    if oppvierkant(zijde) <= 50:
        pkost= oppvierkant(zijde)*20
    elif oppvierkant(zijde) <= 100:
        pkost=oppvierkant(zijde)*18
    elif oppvierkant(zijde):
        pkost=oppvierkant(zijde)*15

    print('plaatsingskosten zijn ',pkost)
    print('De totale kosten zijn ', prijs + prijsgraven + pkost)


elif vorm == 2:
    lengte_rh= int(input('Hoe lang is het zwembad: '))
    breedte_rh= int(input('Hoe breed is het zwembad '))
    if hoogte <= 150:
        if materiaal.lower() == 'hout':
            prijs = opprechthoek(lengte_rh, breedte_rh) * 100
        else:
            prijs = opprechthoek(lengte_rh, breedte_rh) * 115
    elif hoogte > 150:
        if materiaal.lower() == 'hout':
            extra = (hoogte - 150) * 0.02
            prijs = opprechthoek(lengte_rh, breedte_rh) * 100
            prijs += extra * prijs
        else:
            extra = (hoogte - 150) * 0.02
            prijs = opprechthoek(lengte_rh, breedte_rh) * 115
            prijs += extra * prijs
    print('de prijs is', prijs)
    prijsgraven = inhrechthoek(lengte_rh,breedte_rh, (hoogte / 100)) * 60
    print('Prijs graafwerkzaamheden zijn', prijsgraven)
    if opprechthoek(lengte_rh, breedte_rh) <= 50:
        pkost = opprechthoek(lengte_rh, breedte_rh) * 20
    elif opprechthoek(lengte_rh, breedte_rh) <= 100:
        pkost = opprechthoek(lengte_rh, breedte_rh) * 18
    elif opprechthoek(lengte_rh, breedte_rh):
        pkost = opprechthoek(lengte_rh, breedte_rh) * 15

    print('plaatsingskosten zijn ', pkost)
    print('De totale kosten zijn ', prijs + prijsgraven + pkost)

elif vorm == 3:
    straal= int(input('Hoe lang is het zwembad: '))
    if hoogte <= 150:
        if materiaal.lower() == 'hout':
            prijs = oppcirkel(straal) * 100

        else:
            prijs = oppcirkel(straal) * 115
    elif hoogte > 150:
        if materiaal.lower() == 'hout':
            extra = (hoogte - 150) * 0.02
            prijs = oppcirkel(straal) * 100
            prijs += extra * prijs
        else:
            extra = (hoogte - 150) * 0.02
            prijs = oppcirkel(straal) * 115
            prijs += extra * prijs
    print('de prijs is', prijs)
    prijsgraven =  inhcirkel(straal, (hoogte / 100)) * 60
    print('Prijs graafwerkzaamheden zijn', prijsgraven)
    if oppcirkel(straal) <= 50:
        pkost = oppcirkel(straal) * 20
    elif oppcirkel(straal) <= 100:
        pkost = oppcirkel(straal) * 18
    elif oppcirkel(straal):
        pkost = oppcirkel(straal) * 15

    print('plaatsingskosten zijn ', pkost)
    print('De totale kosten zijn ', prijs+prijsgraven+pkost)