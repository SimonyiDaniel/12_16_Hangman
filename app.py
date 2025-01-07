import random
from country_list import get_countries
k+
    countries = get_countries()
    szo_raw = random.choice(countries)
    szo = szo_raw.lower()
    eletek = 7
    blanks = ""
    for i in szo:
        if i != " ":
            blanks += "_ "
        else:
            blanks += "  "

    print(blanks)

    while eletek > 0:
        talalat = input('Találj egy betűt: ').lower()

        if talalat in szo:
            print('Benne van!')
            new_blanks = ""
            for i in range(len(szo)):
                if szo[i] == talalat:
                    new_blanks += talalat + " "
                else:
                    new_blanks += blanks[i*2] + " "
            blanks = new_blanks
        else:
            print('Nincs benne!')
            eletek -= 1

        print(blanks)
        print(f"Életek: {eletek}")

        #minden betut kitalaltak
        if "_" not in blanks:
            print("Gratulálok, kitaláltad a szót!")
            break

    if eletek == 0:
        print("Játék vége, elfogytak az életeid.")
    kerdes = input('Mehet a még egy játék?')