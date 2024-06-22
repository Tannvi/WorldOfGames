import psycopg2

# Database connection details (replace with actual values from your environment)
HOST = "scoresdata"  # Name of the scoresdata service in docker-compose
PORT = 5432
DATABASE = "your_database_name"
USER = "postgres"  # Assuming default user for postgres image
PASSWORD = ${POSTGRES_PASSWORD}  # Replace with your actual password

# Table definition (modify as needed)
TABLE_NAME = "scores"
COLUMNS = ["name", "score"]


def connect_to_db():
    """Connects to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(host=HOST, port=PORT, database=DATABASE, user=USER, password=PASSWORD)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None


def load_data_from_file(conn):
    """Reads data from Scores.txt and populates the table."""
    try:
        cursor = conn.cursor()

        # Open Scores.txt for reading
        with open("Scores.txt", "r") as file:
            # Skip the header row if it exists (modify as needed)
            next(file)
            for line in file:
                data = line.strip().split(",")  # Assuming data is comma-separated

                # Create a placeholder string for the SQL query
                placeholders = ", ".join("%s" for _ in COLUMNS)
                sql = f"INSERT INTO {TABLE_NAME} ({','.join(COLUMNS)}) VALUES ({placeholders})"

                cursor.execute(sql, data)

        conn.commit()
        print("Data loaded successfully!")

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error loading data: {error}")
    finally:
        if cursor:
            cursor.close()


if __name__ == "__main__":
    connection = connect_to_db()
    if connection:
        load_data_from_file(connection)
        connection.close()
    else:
        print("Failed to connect to database!")
