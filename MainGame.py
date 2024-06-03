from Live import load_game, welcome
from MainScores import score_server, app

# Welcome the user
print(welcome("Player"))

# Load and start the game
load_game()

from MainScores import score_server  # Assuming MainScores.py is in the same directory

# ...t your game logic ...

if score_server:
    with app.app_context():  # Create temporary Flask application context
        score_server()


