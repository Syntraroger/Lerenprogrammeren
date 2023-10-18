# Maak een functie toon_resultaat_punten(gehaaldescore,max_score).
# Wanneer de gehaalde score 80 % of meer is komt de tekst in het groen
# Wanneer de score minder dan 50 % is komt de tekst in het rood.
# Tussen de 51 en 79 komt de tekst in het rood
from colorama import Fore
"""
def toon_resultaat_punten(gehaaldescore, max_score):

          percentage = (gehaaldescore*max_score)/max_score
    
        if percentage >= 80:
            print(Fore.GREEN + str(percentage) + Fore.RESET)
        elif percentage > 50 and percentage< 80:
            print(Fore.BLUE + str(percentage) + Fore.RESET)
        elif percentage < 50:
            print(Fore.RED + str(percentage) + Fore.RESET)

toon_resultaat_punten(80, 100)
toon_resultaat_punten(60, 100)
toon_resultaat_punten(44, 100)
"""

def toon_resultaat_punten(gehaaldescore, max_score):

        percentage = round(((gehaaldescore/max_score) * 100),2)

        if percentage >= 80 and percentage < 101:
            print(Fore.GREEN + str(percentage) + Fore.RESET)
        elif percentage >= 50 and percentage < 80:
            print(Fore.BLUE + str(percentage) + Fore.RESET)
        elif percentage < 50:
            print(Fore.RED + str(percentage) + Fore.RESET)
        else:
            print('Onjuiste waarde meer dan 100%, score is hoger dan max score')
for i in range(5):
    gehaaldescore = int(input('geef de score in '))
    maxscore = int(input('geef de max score in '))
    toon_resultaat_punten(gehaaldescore, maxscore)
