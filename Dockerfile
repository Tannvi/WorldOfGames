#Use a slim Python image for a smaller container size
FROM python:3.11-slim

WORKDIR /app

# Copy requirements.txt (if you have one)
COPY requirements.txt ./

# Install dependencies (if using requirements.txt)
RUN pip install -r requirements.txt

# Copy your Flask application code and Scores.txt
COPY . .

# Expose the port where your Flask app listens (replace 5000 if needed)
EXPOSE 5000

# Set the command to run your Flask app (adjust the script name if different)
# Replace with your main script if different
CMD ["python", "MainGame.py"]
