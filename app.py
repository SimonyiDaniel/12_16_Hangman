from country_list import get_countries
import random

countries = get_countries()
print(countries)

country = random.choice(countries)

letters = list(country)

print("Welcome to the Hangman game!")
print(f"The word is {len(country)} long.")
print("Guess a letter!")
print("_ " * len(letters))

