import sqlite3

class Database:
    def __init__(self, db_name='pharmacy.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS medicines (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def add_medicine(self, name, quantity, price):
        self.cursor.execute('''
            INSERT INTO medicines (name, quantity, price) VALUES (?, ?, ?)
        ''', (name, quantity, price))
        self.conn.commit()

    def get_all_medicines(self):
        self.cursor.execute('SELECT * FROM medicines')
        return self.cursor.fetchall()

    def update_medicine(self, medicine_id, name, quantity, price):
        self.cursor.execute('''
            UPDATE medicines SET name = ?, quantity = ?, price = ? WHERE id = ?
        ''', (name, quantity, price, medicine_id))
        self.conn.commit()

    def delete_medicine(self, medicine_id):
        self.cursor.execute('DELETE FROM medicines WHERE id = ?', (medicine_id,))
        self.conn.commit()
