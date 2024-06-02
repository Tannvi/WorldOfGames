from Live import load_game, welcome
from MainScores import score_server, app

# Get username (optional)
user_name = input("Enter your name (or press Enter to continue): ")

# Print welcome message
print(welcome(user_name if user_name else "Player"))  # Use user name if provided, otherwise default to "Player"

# Load and start the game
load_game()

from MainScores import score_server  # Assuming MainScores.py is in the same directory

# ...t your game logic ...

if score_server:
    with app.app_context():  # Create temporary Flask application context
        score_server()


