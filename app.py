from country_list import get_countries
import random

countries = get_countries()
country = random.choice(countries)
print(country)
letters = list(country)

guesses = ["_ " * len(country)]

lives = 7

print("Welcome to the Hangman game!")
print('You have 7 lives, try to guess the country without losing them')
print(f"The word is {len(country)} long.")

while True:
    guessed_letter = str(input("Guess a letter!"))

    if guessed_letter in letters:
        print("helje")
    else:
        print("kaki")