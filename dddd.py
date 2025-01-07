import random
from country_list import countries_for_language

def play_hangman():
    # Országok listájának lekérése (angol nyelvű országnevekkel)
    countries = countries_for_language('hu')
    word_list = [country.lower() for code, country in countries]  # Országnevek kisbetűs formában
    
    # Véletlenszerű ország kiválasztása a listából
    word_to_guess = random.choice(word_list)
    guessed_letters = set()
    wrong_guesses = set()
    attempts = 6  # Ennyi élet van a játék kezdetén

    def display_word(word, guessed_letters):
        return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

    print("Akasztófa játék kezdődik! A szavak országnevek.")
    print(f"A kitalálandó szó {len(word_to_guess)} betű hosszú.")

    while attempts > 0:
        print("\nJelenlegi állapot:", display_word(word_to_guess, guessed_letters))
        print(f"Maradék próbálkozások: {attempts}")
        print(f"Hibás találgatások: {', '.join(sorted(wrong_guesses)) if wrong_guesses else 'Nincsenek hibás találgatások.'}")

        guess = input("Tippelj egy betűt (vagy írd be, hogy 'quit' a kilépéshez): ").lower()

        if guess == "quit":
            print("Kiléptél a játékból. Viszlát!")
            break

        if len(guess) != 1 or not guess.isalpha():
            print("Kérlek, csak egy betűt adj meg!")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            print("Ezt a betűt már tippelted korábban.")
            continue

        if guess in word_to_guess:
            print("Helyes tipp!")
            guessed_letters.add(guess)
        else:
            print("Rossz tipp.")
            wrong_guesses.add(guess)
            attempts -= 1

        # Ellenőrizzük, hogy minden betűt kitalált-e
        if all(letter in guessed_letters for letter in word_to_guess):
            print(f"\nGratulálok, nyertél! A kitalálandó szó: {word_to_guess}")
            break
    else:
        print(f"Vesztettél! A szó az volt: {word_to_guess}")

if __name__ == "__main__":
    play_hangman()