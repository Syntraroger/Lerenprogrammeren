# Genereer een lijst met 20 punten tussen 1 en 100
# Punten tussen 0 en 30, kleur rood(feedback zware onvoldoende)
# Punten tussen 31 en 49 ,kleur oranje(feedback onvoldoende)
# Punten tussen 50 en 75, kleur blauw(feedback geslaagd)
# Punten tussen 76 en 100, kleur groen(feedback geslaagd met onderscheiding)
# Doorloop de lijst en laat de feedback doorlopen.
# Geef daarna ook het aantal geslaagde > 50
import random
from colorama import Fore

def punten():
    lijst=[]
    for i in range(20):
        lijst.append(round(random.uniform(1, 100),0))
    lijst.sort()
    for i in range(len(lijst)):
        if lijst[i] <= 30:
            print(Fore.RED + str(lijst[i]) + ' Zware Onvoldoende'+ Fore.RESET)
            # lijst[i] = (Fore.RED + str(lijst[i]) + ' Zware Onvoldoende'+ Fore.RESET)
        elif lijst[i] > 30 and lijst[i] <= 49:
            print(Fore.YELLOW + str(lijst[i]) + ' Onvoldoende'+ Fore.RESET)
        elif lijst[i] >= 50 and lijst[i] <= 75:
            print(Fore.BLUE + str(lijst[i]) + ' Geslaagd '+ Fore.RESET)
        elif lijst[i] > 75 and lijst[i] <= 100:
            print(Fore.GREEN + str(lijst[i]) + ' Geslaagd met onderscheiding'+ Fore.RESET)

    lijst50=[]
    for i in range(len(lijst)):
        if lijst[i] >= 50:
            lijst50.append(lijst[i])
    print(lijst50)
    print(repr(lijst50))
    print(help(repr))


punten()

