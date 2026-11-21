# Kenny Chambers
# CIS256 FALL 2026
# Programming Assignment 4

import random

# List of words chosen at random during the game.
WORDS = ["retro", "stellar", "interscope", "unknown"]
# Maximum of incorrect guesses that user can make in the game
MAX_WRONG_GUESSES = 7

def play_game():
    # Randomly selects word from the predefined list above.
    word = random.choice(WORDS)
    # Tracks/records letter user inputted for guesses.
    guessed_letters = set()
    # Counts the incorrect guesses accordingly.
    wrong_guesses = 0

    print("Welcome to the mystical world of World Planet Guesser!")
    print(f'You are lucky enoguht to make up to a maximum of {MAX_WRONG_GUESSES} wrong guesses.')
    print("If you reached the maximum of worng guesses... well the intergalactic federation is going to destroy your home planet! No pressure!")

    # Game keeps playing until maximum incorrect guesses has been reached.
    while wrong_guesses < MAX_WRONG_GUESSES:
        # Builds display string for instances of the guessed letters wiht underscores for the unguessed letters.
        display = " ".join(letter if letter in guessed_letters else "_" for letter in word)
        print(f'\nWord: {display}')
        print(f'Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}')

        # Retreives user inputs on guesses, while ingoring spaces and lettercase.
        guess = input("Guess one letter for the safety of Earth: ").strip().lower()

        # Validates input.
        if len(guess) != 1 or not guess.isalpha():
            print("Unfortunately, that is not a single letter! Please enter a letter.")
            continue
        # Prevents repeated guesses from penalizing the user.
        if guess in guessed_letters:
            print("Already used letter.")
            continue

        # Records user's new guess.
        guessed_letters.add(guess)

        # Display if the letter meets the letter within the random word.
        if guess in word:
            print("Correcto! Letter has matched the mystery word, closer to saving your planet!")
            # Win condition. All letters in the word have been guessed.
            if all(letter in guessed_letters for letter in word):
                print(f'\nCongratulations! You are the planetary savior of Earth. Word guessed was: {word}')
                return
            # Incorrect guesses, acts as one attempt.
        else:
            wrong_guesses += 1
            print("INCORRECT!")
    # Loop ended without guessing all the letters to the word.
    print(f'\nUnfortunately, you ran out of attempts to guess the word! The word was {word}. We will allow you collect your affairs and say goodbye to your loved ones')
    print("Please allow the federation to charge the death beam, may take around 1,000 years to warm up. In the meantime, sit back and relax.")

if __name__ == "__main__":
    play_game()