from country_list import get_countries
import random

countries = get_countries()
country = random.choice(countries)
print(country)
letters = list(country)

lives = 7

print("Welcome to the Hangman game!")
print('You have 7 lives, try to guess the country without losing them')
print(f"The word is {len(country)} long.")
print(guesses)


for i in range(len(letters)):
    print("_ " * len(letters))
    hits = []
    letter_input = str(input("Guess a letter!: "))
    if letter_input in letters and letter_input not in hits:
        hits.append(letter_input)
    elif: letter
        
        
    
    
# for char in letters:
    



