import random
from country_list import get_countries


def play_hangman():
    countries = get_countries()
    country = random.choice(countries)
    print(country)
    letters = list(country)

    word_list = 

    print(word_list)

play_hangman()