from database.py import Database
from models import Medicine

def main():
    db = Database()

    # Add a new medicine
    db.add_medicine('Paracetamol', 100, 1.99)

    # Get and print all medicines
    medicines = db.get_all_medicines()
    for med in medicines:
        print(f'ID: {med[0]}, Name: {med[1]}, Quantity: {med[2]}, Price: {med[3]}')

if __name__ == '__main__':
    main()
