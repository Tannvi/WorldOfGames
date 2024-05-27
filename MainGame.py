from Live import load_game, welcome

# Welcome the user
print(welcome("Guy"))

# Load the game and get user choices
game_choice, difficulty_level = load_game()

# Print user selections (optional)
print(f"\nYou chose game {game_choice} with difficulty {difficulty_level}")

# Call the specific game function based on the user's choice (not implemented here)
# This part would likely involve additional logic and potentially other Python files
# for each game

# Example (placeholder):
if game_choice == 1:
  print("Starting Memory Game...")
  # Implement Memory Game logic here
else:
  print(f"Game {game_choice} is not yet implemented.")
