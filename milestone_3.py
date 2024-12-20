import random

# Original list of possible secret words
secret_words = ["watermelon", "mango", "pomegranate", "strawberry", "pineapple"]

# Randomly choose a secret word
secret_word = random.choice(secret_words)

# Step 1: Function to check if the guessed letter is in the secret word
def check_guess(guess):
    # Convert the guess to lowercase
    guess = guess.lower()

    # Check if the guess is in the secret word
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# Step 2: Function to ask the user for a valid guess
def ask_for_input():
    while True:
        # Ask the user to guess a letter
        guess = input("Please guess a letter: ")

        # Check if the guess is a valid single alphabetical character
        if guess.isalpha() and len(guess) == 1:
            # Call the check_guess function to see if the guess is in the word
            check_guess(guess)
            break  # Exit the loop after a valid guess
        else:
            # If the input is invalid, ask the user to try again
            print("Invalid letter. Please, enter a single alphabetical character.")

# Step 3: Call the ask_for_input function to test the code
ask_for_input()




