import time
import os
import psycopg2
from psycopg2 import sql

DB_HOST = os.getenv("POSTGRES_HOST", "my-postgres")
DB_NAME = os.getenv("POSTGRES_DB", "mydb")
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "pass")
DB_PORT = int(os.getenv("POSTGRES_PORT", 5432))

def wait_for_db(retries=10, delay=2):
    for i in range(retries):
        try:
            conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
            conn.close()
            print("Postgres is ready.")
            return True
        except Exception as e:
            print(f"Postgres not ready yet ({i+1}/{retries}): {e}")
            time.sleep(delay)
    return False

def main():
    if not wait_for_db():
        print("Could not connect to Postgres. Exiting.")
        return

    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS, port=DB_PORT)
        cur = conn.cursor()

        # Create table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS people (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)

        # Insert a row
        cur.execute("INSERT INTO people (name) VALUES (%s) RETURNING id;", ("Rahul Sayya",))
        new_id = cur.fetchone()[0]
        conn.commit()
        print(f"Inserted row id: {new_id}")

        # Read the row
        cur.execute("SELECT id, name, created_at FROM people WHERE id = %s;", (new_id,))
        row = cur.fetchone()
        print("Read row from DB:", row)

        cur.close()
        conn.close()
    except Exception as e:
        print("Error during DB ops:", e)

if __name__ == "__main__":
    main()
