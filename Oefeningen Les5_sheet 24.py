# Maak een functie toon_resultaat_punten(gehaaldescore,max_score).
# Wanneer de gehaalde score 80 % of meer is komt de tekst in het groen
# Wanneer de score minder dan 50 % is komt de tekst in het rood.
# Tussen de 51 en 79 komt de tekst in het blauw

from colorama import Fore


def toon_resultaat_punten(gehaaldescore, max_score):
    if max_score >= 80:
        print(Fore.GREEN + str(gehaaldescore) + Fore.RESET)
    elif max_score < 50:
        print(Fore.RED + str(gehaaldescore) + Fore.RESET)
    else:
        print(Fore.BLUE + str(gehaaldescore) + Fore.RESET)

toon_resultaat_punten('De score voor wiskunde is meer dan 80%' , 80)
toon_resultaat_punten('De score voor Nederlands is gemiddeld' , 70)
toon_resultaat_punten('De score voor Engels is minder dan 50%' , 48)

