from MemoryGame import MemoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRouletteGame
from Score import difficulty


def welcome(name):
  """Greets the user by name and welcomes them to the World of Games."""
  return f"Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play."

def load_game():
  """Prompts user for game selection and difficulty level, then starts the chosen game."""
  print("Please choose a game to play:")
  print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
  print("2. Guess Game - guess a number and see if you chose like the computer")
  print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

  while True:
    try:
      game_choice = int(input("Enter game number (1-3): "))
      if 1 <= game_choice <= 3:
        break
      else:
        print("Invalid game choice. Please enter a number between 1 and 3.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  print("\nPlease choose game difficulty from 1 to 5:")

  while True:
    try:
      difficulty_level = int(input("Enter difficulty level (1-5): "))
      if 1 <= difficulty_level <= 5:
        break
      else:
        print("Invalid difficulty level. Please enter a number between 1 and 5.")
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Start the chosen game based on selection
  if game_choice == 1:
    game = MemoryGame(difficulty_level)
  elif game_choice == 2:
    game = GuessGame(difficulty_level)
  elif game_choice == 3:
    game = CurrencyRouletteGame(difficulty_level)
  else:
    print("An unexpected error occurred. Please try again.")
    return  # Exit the function if an invalid choice is made internally

  # Play the game

  # Check if the user won the game (replace with your winning condition)
  win = game.play()
  if win:
    try:
      # Import add_score function for better modularity
      from Score import add_score

      # User won, call add_score function (replace game_score with the actual score obtained)
      add_score(difficulty)
      print("Congratulations! You won and your score has been updated.")
    except (ImportError, FileNotFoundError, ValueError) as e:
      print(f"Error updating score: {e}")
      print("Continuing the game...")  # Consider user preference (continue/exit)



# Example usage (uncomment to test)
name = input("Enter your name: ")
print(welcome(name))
load_game()
