# Importera funktionen choice ifrån modulen random och skriv en egen funktion
# som tar emot en lista med val, väljer ut ett slumpat element och skriver ut
# det valda elementet.

# Koden nedan är enbart för att kontrollera att övningen är rätt; ändra anropen
# så att de anropar din funktion.

import random
import numpy as np

def rnd_choice(a_list: list):
    return random.choice(a_list)

def rnd_choice_np(a_list: list, N = 1):
    return np.random.choice(a_list, size=N)


print(rnd_choice([1, 2, 3, 4]))
print(rnd_choice(["Ett", "Två", "Tre"]))
print(rnd_choice([1, "Två", 3, "Fyra"]))

print()
print(rnd_choice_np([1, "Två", 3, "Fyra"], 2))
