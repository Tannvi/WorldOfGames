import random
import requests

class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def get_exchange_rate(self):
        """Fetches the current USD to ILS exchange rate from an API."""
        url = "https://api.exchangerate.host/latest?base=USD&symbols=ILS"
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-200 status codes
        data = response.json()
        return data["rates"]["ILS"]

    def get_money_interval(self):
        """Generates a random amount of USD and calculates the ILS interval."""
        amount_usd = random.randint(1, 100)
        exchange_rate = self.get_exchange_rate()
        amount_ils = amount_usd * exchange_rate
        interval_width = 5 - self.difficulty
        return (amount_ils - interval_width, amount_ils + interval_width)

    def get_guess_from_user(self, amount_usd):
        """Prompts the user for a guess in ILS and validates it."""
        while True:
            try:
                guess_ils = float(input(f"Guess the value of ${amount_usd:.2f} in ILS: "))
                return guess_ils
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play(self):
        """Runs the game loop."""
        interval = self.get_money_interval()
        amount_usd = random.randint(1, 100)  # Regenerate a new amount of USD

        guess_ils = self.get_guess_from_user(amount_usd)
        correct_ils = amount_usd * self.get_exchange_rate()

        return interval[0] <= guess_ils <= interval[1]

