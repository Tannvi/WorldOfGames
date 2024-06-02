from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

POINTS_PER_WIN = lambda difficulty: (difficulty * 3) + 5  # Function to calculate points

def read_score():
    """Reads the current score from the scores file (if it exists)."""
    try:
        with open(SCORES_FILE_NAME, 'r') as f:
            score = int(f.read().strip())
            return score
    except (FileNotFoundError, ValueError):
        return 0  # Return 0 if file doesn't exist or contains invalid data

def write_score(score):
    """Writes the current score to the scores file."""
    try:
        with open(SCORES_FILE_NAME, 'w') as f:
            f.write(str(score))
    except Exception as e:
        print(f"Error writing score to file: {e}")
        return BAD_RETURN_CODE  # Indicate an error

def add_score(difficulty):
    """Adds the score earned based on difficulty to the current score and saves it."""
    current_score = read_score()
    points_earned = POINTS_PER_WIN(difficulty)
    new_score = current_score + points_earned
    write_score(new_score)
    return new_score
