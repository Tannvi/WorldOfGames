import random

class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = self.generate_number()

    def generate_number(self):
        """Generates a random number between 1 and the difficulty."""
        return random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        """Prompts the user for a guess and validates it."""
        while True:
            try:
                guess = int(input("Guess a number between 1 and {}: ".format(self.difficulty)))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print("Invalid guess. Please enter a number within the range.")
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def compare_results(self, guess):
        """Compares the user's guess with the secret number."""
        if guess == self.secret_number:
            return True
        else:
            return False

    def play(self):
        """Runs the game loop."""
        while True:
            guess = self.get_guess_from_user()
            if self.compare_results(guess):
                print("Congratulations, you guessed it!")
                break
            else:
                print("Incorrect guess. Try again.")









