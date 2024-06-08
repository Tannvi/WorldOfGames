import requests
from bs4 import BeautifulSoup  # For basic HTML parsing


def test_scores_service(url):
    """Tests the score service by fetching the score and validating its format."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching score: {e}")
        return False

    # Assuming the score is displayed within a div with id "score"
    soup = BeautifulSoup(response.content, "html.parser")
    score_element = soup.find(id="score")

    if score_element is None:
        print("Score element not found in the response.")
        return False

    try:
        score = int(score_element.text.strip())
    except ValueError:
        print("Score is not a valid number.")
        return False

    if not (1 <= score <= 1000):
        print(f"Score value ({score}) is outside the expected range (1-1000).")
        return False

    # Score is valid
    print(f"Score retrieved successfully: {score}")
    return True

    # Example usage (uncomment to test)
    # Replace with the actual URL of your deployed score service
    service_url = "http://localhost:5000/"  # Assuming Flask app runs on port 5000
    if test_scores_service(service_url):
        print("Score service test passed!")
    else:
        print("Score service test failed!")


def main():
    """Calls the score service test and returns an exit code based on the result."""
    # Replace with the actual URL of your deployed score service
    service_url = "http://localhost:5000/"  # Assuming Flask app runs on port 5000
    if test_scores_service(service_url):
        return 0  # Test passed
    else:
        return -1  # Test failed


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)
