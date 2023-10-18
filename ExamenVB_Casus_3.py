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



def oppvierkant(lengte, hoogte ):
    opp = lengte*hoogte*4
    return opp
def inhoudvierkant(lengte, hoogte):
    inh = lengte*lengte*hoogte
    return inh

def opprechthoek(lengte, breedte, hoogte):
    oppl = lengte*hoogte
    oppb = breedte* hoogte
    opp = oppl+oppb
    return opp
def inhoudrechthoek(lengte, breedte, hoogte):
    inh = lengte * breedte* hoogte
    return inh

def oppovaal(straal, lengte, hoogte):

prijshout = 100
prijsstaal = 150
graafm3 = 60

