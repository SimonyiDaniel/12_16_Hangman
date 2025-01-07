import random
from lists.contry_and_capital_list import countries_and_capitals
from lists.ascii import HANGMANPICS
kepek = HANGMANPICS
def gamemode2():
    print('Ebben a játékmódban nem csak az országot kell kitalálni, hanem a fővárost is! ( a főváros a "|" jel után lesz)') 
    kerdes = input('Készen állsz?')
    while kerdes.lower() not in ['nem', 'no', '❌']:
        countries = countries_and_capitals()
        szo_raw = random.choice(countries)
        szo = szo_raw.lower()
        eletek = 7
        blanks = ''
        
        for i in szo:
            if i == ' ':
                blanks += '  '
            elif i == '|':
                blanks += '| '
            else:
                blanks += '_ '

        print(blanks)

        while eletek > 0:
            talalat = input('Találj egy betűt: ').lower()

            if talalat in szo:
                print('Benne van!')
                new_blanks = ""
                for i in range(len(szo)):
                    if szo[i] == talalat:
                        new_blanks += talalat + " "
                    elif szo[i] == '|':
                        new_blanks += '| '
                    elif szo[i] == ' ':
                        new_blanks += '  '
                    else:
                        new_blanks += blanks[i * 2] + " "
                blanks = new_blanks
            else:
                print('Nincs benne!')
                eletek -= 1
                print(kepek[7 - eletek])

            print(blanks)
            print(f'Életek: {eletek},')

            if "_" not in blanks:
                print('Gratulálok, kitaláltad a szót!')
                break

        if eletek == 0:
            print(f'Játék vége, elfogytak az életeid. A helyes válasz {szo} volt.')
        
        kerdes = input('Mehet még egy játék ezen a nehézségen?')