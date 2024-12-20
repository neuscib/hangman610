import random

class Hangman:
    def __init__(self, word_list):
        self.word_list = word_list
        self.num_lives = 5
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.list_of_guesses.append(guess)

    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print(f"You already tried {guess}.")
            else:
                self.check_guess(guess)
                break

    def is_game_over(self):
        if self.num_lives <= 0:
            print("Game over! You've lost.")
            return True
        elif self.num_letters == 0:
            print("You guessed the word! Congratulations!")
            return True
        return False

if __name__ == "__main__":
    word_list = ["watermelon", "mango", "pomegranate", "strawberry", "pineapple"]
    game = Hangman(word_list)

    while not game.is_game_over():
        print(" ".join(game.word_guessed))
        game.ask_for_input()
