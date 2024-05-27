from flask import Flask, render_template

from Score import read_score, BAD_RETURN_CODE

app = Flask(__name__)

@app.route("/")
def serve_score():
  """Reads the score from file and returns an HTML response."""
  try:
    score = read_score()
    if score == BAD_RETURN_CODE:
      # Error reading score, display error message
      return render_template("score.html", score="Error reading score")
    else:
      return render_template("score.html", score=score)
  except Exception as e:
    print(f"Unexpected error: {e}")
    return render_template("score.html", score="Internal server error")

if __name__ == "__main__":
  app.run(debug=True)  # Run in debug mode for development (optional)


