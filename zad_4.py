import random
import os


wygrane = 0
proby = 0
pkn = ['p', 'k', 'n']

while True:
    print("\tPKN\n")
    print("Twój wynik:", wygrane,"\\",proby,"\n\n")
    print("[p] Papier\n[k] Kamień\n[n] Nożyce\n\n Wybierz znak!")
    proba = input("   ").lower()

    if proba in pkn:
        komputer = random.choice(pkn)

        if proba == komputer:
            print("\n+-----------------+\n     REMIS\n+-----------------+")
            proby += 1

        elif (proba == 'p' and komputer == 'k') or (proba == 'n' and komputer == 'p') or (proba == 'k' and komputer == 'n'):
            print("\n+-----------------+\n     WYGRANA\n+-----------------+")
            proby += 1
            wygrane += 1

        else:
            print("\n+-----------------+\n     PRZEGRANA\n+-----------------+")
            proby += 1

    else:
        print("\tDafuk?!\n Wybierz jeden z poniższych:\n   'p', 'k', 'n'")

    raz = input("\n\nJeszcze raz? [y/n]")

    if raz.lower() == 'n':
        break

    os.system('clear')
