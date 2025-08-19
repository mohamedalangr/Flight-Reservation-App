# database.py
import sqlite3
from contextlib import closing

SCHEMA = """
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    flight_number TEXT NOT NULL,
    departure TEXT NOT NULL,
    destination TEXT NOT NULL,
    date TEXT NOT NULL,
    seat_number TEXT NOT NULL
);
"""

class Database:
    def __init__(self, db_path: str = "flights.db"):
        self.db_path = db_path
        self._init_db()

    def _get_conn(self):
        return sqlite3.connect(self.db_path)

    def _init_db(self):
        with self._get_conn() as conn:
            conn.execute(SCHEMA)
            conn.commit()

    # CRUD operations
    def add_reservation(self, name, flight_number, departure, destination, date, seat_number):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
                   VALUES (?, ?, ?, ?, ?, ?)""",
                (name, flight_number, departure, destination, date, seat_number),
            )
            conn.commit()
            return cur.lastrowid

    def list_reservations(self):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""SELECT id, name, flight_number, departure, destination, date, seat_number
                           FROM reservations ORDER BY id DESC""")
            return cur.fetchall()

    def get_reservation(self, reservation_id: int):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("""SELECT id, name, flight_number, departure, destination, date, seat_number
                           FROM reservations WHERE id = ?""", (reservation_id,))
            return cur.fetchone()

    def update_reservation(self, reservation_id: int, name, flight_number, departure, destination, date, seat_number):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                """UPDATE reservations
                   SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
                   WHERE id=?""",
                (name, flight_number, departure, destination, date, seat_number, reservation_id),
            )
            conn.commit()
            return cur.rowcount

    def delete_reservation(self, reservation_id: int):
        with self._get_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
            conn.commit()
            return cur.rowcount
