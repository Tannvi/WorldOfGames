import random
import time

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        """Generates a list of random numbers between 1 and 101."""
        return random.sample(range(1, 101), self.difficulty)

    def display_sequence(self, sequence):
        """Clears the screen and displays the sequence for 0.7 seconds."""
        print("\n" * 100)  # Clear the screen
        for number in sequence:
            print(number, end=" ")
            time.sleep(0.7)
        print("\n")  # Add a newline for visual clarity

    def get_list_from_user(self):
        """Prompts the user for a list of numbers and validates them."""
        user_list = []
        while len(user_list) < self.difficulty:
            try:
                number = int(input("Enter a number you remember ({} left): ".format(self.difficulty - len(user_list))))
                user_list.append(number)
            except ValueError:
                print("Invalid input. Please enter a whole number.")
        return user_list

    def is_list_equal(self, list1, list2):
        """Compares two lists for equality."""
        return list1 == list2

    def play(self):
        """Runs the game loop."""
        sequence = self.generate_sequence()
        self.display_sequence(sequence)

        user_list = self.get_list_from_user()
        return self.is_list_equal(sequence, user_list)
