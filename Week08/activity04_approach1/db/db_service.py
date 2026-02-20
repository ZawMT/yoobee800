import sqlite3
import sys
import json

DB_NAME = "/data/cars.db"


class CarDatabase:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name

    def _connect(self):
        return sqlite3.connect(self.db_name)

    # Creating the table to keep car records
    def create_table(self):
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS cars (
                    plate TEXT PRIMARY KEY,
                    car_type TEXT NOT NULL,
                    year INTEGER NOT NULL CHECK(year >= 1886)
                )
            """)
            conn.commit()

    # Adding a car to the table
    def add_car(self, plate, car_type, year):
        with self._connect() as conn:
            cur = conn.cursor()
            try:
                cur.execute(
                    "INSERT INTO cars VALUES (?, ?, ?)",
                    (plate, car_type, year)
                )
                conn.commit()
                print("OK")
            except sqlite3.IntegrityError:
                print("EXISTS")

    # Listing all the cars in the table
    def list_cars(self):
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT plate, car_type, year FROM cars")
            rows = cur.fetchall()
            print(json.dumps(rows))

    # Removing a car from the table
    def remove_car(self, plate):
        with self._connect() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM cars WHERE plate=?", (plate,))
            conn.commit()
            print("OK" if cur.rowcount else "NOTFOUND")


if __name__ == "__main__":
    db = CarDatabase()
    db.create_table()

    cmd = sys.argv[1]

    '''
    The database functions are provided as parameterised commands
    '''
    if cmd == "add":
        db.add_car(sys.argv[2], sys.argv[3], int(sys.argv[4]))
    elif cmd == "list":
        db.list_cars()
    elif cmd == "remove":
        db.remove_car(sys.argv[2])
