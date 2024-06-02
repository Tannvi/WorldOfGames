from Score import read_score, BAD_RETURN_CODE
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def score_server():
    """
  Reads the score from scores.txt and returns an HTML template.

  Returns:
      str: Rendered HTML template with the score or an error message.
  """
    try:
        with open("Scores.txt", "r") as f:
            score = int(f.read())
    except (FileNotFoundError, ValueError) as e:
        error = f"Error reading score: {e}"
        return render_template("score.html", score=None, error=error)

    return render_template("score.html", score=score, error=None)


if __name__ == "__main__":
    app.run(debug=True)
