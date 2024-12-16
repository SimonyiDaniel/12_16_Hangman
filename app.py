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
while True:
    guessed_letter = str(input("Guess a letter!"))

    #if guessed_letter.lower() in letters:
        #index = letters.index(guessed_letter)
        #guesses[index] = guessed_letter
        #print(guesses)
    #else:
        #print("kaki")

    
for index, guessed_letter in enumerate(letters):
        guesses[index] = guessed_letter

print(guesses)  

for i in range(len(letters)):
    print(guesses)
    letter_input = str(input("Guess a letter!: "))
    if letter_input in letters
    
    
# for char in letters:
    



