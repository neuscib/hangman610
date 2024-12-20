import random

# Define the Hangman class
class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list = word_list
        self.num_lives = num_lives
        self.secret_word = random.choice(self.word_list).lower()
        self.guessed_letters = []
        self.num_letters = len(self.secret_word)

    def display_word(self):
        # Display the current word with guessed letters and underscores for unguessed letters
        word_display = "".join([letter if letter in self.guessed_letters else "_" for letter in self.secret_word])
        print("Current word: " + " ".join(word_display))
        return word_display

    def ask_for_input(self):
        # Ask the user to guess a letter and validate it
        guess = input("Guess a letter: ").lower()
        while not (guess.isalpha() and len(guess) == 1):
            print("Invalid input. Please enter a single letter.")
            guess = input("Guess a letter: ").lower()
        return guess

    def check_guess(self, guess):
        # Check if the guessed letter is in the secret word
        if guess in self.guessed_letters:
            print("You already guessed that letter.")
        elif guess in self.secret_word:
            self.guessed_letters.append(guess)
            print(f"Good guess! {guess} is in the word.")
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
        
    def is_game_won(self):
        # Check if all letters in the word have been guessed
        return set(self.secret_word).issubset(set(self.guessed_letters))


# Define the play_game function
def play_game(word_list):
    num_lives = 5  # Set the number of lives to 5
    game = Hangman(word_list, num_lives)  # Create a new instance of Hangman
    print("Welcome to Hangman!")
    
    while True:
        # Display the current word
        word_display = game.display_word()
        
        # Check if the user lost
        if game.num_lives == 0:
            print(f"You lost! The word was: {game.secret_word}")
            break
        
        # Check if the user has guessed all letters correctly
        if game.is_game_won():
            print("Congratulations! You won the game!")
            break
        
        # Ask the user for a new guess
        guess = game.ask_for_input()
        
        # Check if the guess is correct and update game state
        game.check_guess(guess)


# Word list for the game
word_list = ["watermelon", "mango", "pomegranate", "strawberry", "pineapple"]

# Call the play_game function
play_game(word_list)
