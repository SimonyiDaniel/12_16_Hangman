import random
from lists.contry_and_capital_list import countries_and_capitals
from lists.ascii import HANGMANPICS
from app import gamemode1
from app_hard import gamemode2
kepek = HANGMANPICS
print('Üdvözöllek a "Hangman country edition" játékban!🙋‍♂️🙋‍♂️')
start = input('Mehet a játék?❌✔\n')
if start.lower() not in ['no', 'nem', '❌']:
    gm = input('Válasz nehézségi szintet \nnormál - 1 \nnehéz - 2\n')
if gm == '1':
    gamemode1() 
elif gm == '2':
    gamemode2()
else:
    print('Helytelen nehézségi szint választás')