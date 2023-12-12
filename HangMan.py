import random

# List of words for the Hangman game
words = ['apple', 'banana', 'orange', 'strawberry', 'grape', 'watermelon', 'pineapple', 'blueberry']

# Function to choose a random word from the list
def choose_word(words):
    return random.choice(words)

# Function to play Hangman
def hangman():
    secret_word = choose_word(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the secret word.")

    while attempts > 0:
        display_word = ''
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += '_'

        print(f"\nWord: {display_word}")
        print(f"Attempts left: {attempts}")
        
        if display_word == secret_word:
            print("\nCongratulations! You guessed the word!")
            break

        guess = input("Enter a letter or the whole word: ").lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Oops! That letter is not in the word.")
                attempts -= 1
        else:
            if guess == secret_word:
                print("\nCongratulations! You guessed the word!")
                break
            else:
                print("That's not the word. Try again!")
                attempts -= 1

    else:
        print("\nSorry, you've run out of attempts. The word was:", secret_word)

# Start the Hangman game
hangman()

