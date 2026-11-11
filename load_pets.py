
import sqlite3

def main():
    # Connect to the SQLite database
    connection = sqlite3.connect("pets.db")
    cursor = connection.cursor()

    # Create the person table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
        )
    """)

    # Create the pet table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pet (
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT,
            age INTEGER,
            dead INTEGER
        )
    """)

    # Create the relationship table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS person_pet (
            person_id INTEGER,
            pet_id INTEGER
        )
    """)

    # Insert people
    people = [
        (1, "James", "Smith", 41),
        (2, "Diana", "Greene", 23),
        (3, "Sara", "White", 27),
        (4, "William", "Gibson", 23)
    ]

    # Insert pets
    pets = [
        (1, "Rusty", "Dalmation", 4, 1),
        (2, "Bella", "Alaskan Malamute", 3, 0),
        (3, "Max", "Cocker Spaniel", 1, 0),
        (4, "Rocky", "Beagle", 7, 0),
        (5, "Rufus", "Cocker Spaniel", 1, 0),
        (6, "Spot", "Bloodhound", 2, 1)
    ]

    # Connect people to their pets
    relationships = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    ]

    cursor.executemany(
        "INSERT OR REPLACE INTO person VALUES (?, ?, ?, ?)",
        people
    )

    cursor.executemany(
        "INSERT OR REPLACE INTO pet VALUES (?, ?, ?, ?, ?)",
        pets
    )

    # Clear existing relationships to avoid duplicates
    cursor.execute("DELETE FROM person_pet")

    cursor.executemany(
        "INSERT INTO person_pet VALUES (?, ?)",
        relationships
    )

    connection.commit()
    connection.close()

    print("Pets database created and populated successfully!")


if __name__ == "__main__":
    main()

