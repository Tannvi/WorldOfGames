SCORES_FILE_NAME = "Scores.txt"  # File name for storing scores (if needed)
BAD_RETURN_CODE = -1  # Represents an error condition in a function

def clear_screen():
    """Clears the terminal screen."""
    import os
    if os.name == "nt":  # Windows
        os.system("cls")
    else:
        os.system("clear")  # Linux/macOS

# Example usage (uncomment to test)
clear_screen()
