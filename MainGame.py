from Live import load_game, welcome
from MainScores import score_server, app
import os
import time

welcome('name')

# Load and start the game
load_game()

if __name__ == '__main__':
    user_name = os.getenv('USER_NAME', 'default_user')
    print(welcome(user_name))
    load_game()
    # Keep the application running
    while True:
<<<<<<< Updated upstream
        time.sleep(400)
=======
        time.sleep(10)

from MainScores import score_server  # Assuming MainScores.py is in the same directory
>>>>>>> Stashed changes


from MainScores import score_server  # Assuming MainScores.py is in the same directory

if score_server:
    with app.app_context():  # Create temporary Flask application context
        score_server()


