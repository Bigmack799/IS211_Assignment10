
import sqlite3
from pathlib import Path


def main():
    # Locate the database in the same folder as this script
    database_path = Path(__file__).resolve().parent / "pets.db"

    if not database_path.is_file():
        print("Error: pets.db was not found. Run load_pets.py first.")
        return

    # Connect to the existing pets database
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()

    print("Welcome to the Pets Database!")
    print("Enter a person's ID to view their pets.")
    print("Enter -1 to exit.\n")

    try:
        while True:
            user_input = input("Enter a person's ID (-1 to exit): ")

            # Validate user input
            try:
                person_id = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a number.\n")
                continue

            # Exit the program when -1 is entered
            if person_id == -1:
                print("Exiting program.")
                break

            # Find the person by ID
            cursor.execute("""
                SELECT first_name, last_name, age
                FROM person
                WHERE id = ?
            """, (person_id,))

            person = cursor.fetchone()

            # Handle nonexistent person IDs
            if person is None:
                print(f"Error: No person found with ID {person_id}.\n")
                continue

            first_name, last_name, age = person
            full_name = f"{first_name} {last_name}"

            print(f"\n{full_name}, {age} years old.")

            # Retrieve pets through the relationship table
            cursor.execute("""
                SELECT pet.name, pet.breed, pet.age, pet.dead
                FROM pet
                JOIN person_pet
                    ON pet.id = person_pet.pet_id
                WHERE person_pet.person_id = ?
                ORDER BY pet.id
            """, (person_id,))

            pets = cursor.fetchall()

            if not pets:
                print(f"{full_name} has no pets listed.")
            else:
                for name, breed, pet_age, dead in pets:
                    article = "an" if breed[0].lower() in "aeiou" else "a"

                    if dead == 1:
                        print(
                            f"{full_name} owned {name}, "
                            f"{article} {breed}, "
                            f"that was {pet_age} years old (deceased)."
                        )
                    else:
                        print(
                            f"{full_name} owns {name}, "
                            f"{article} {breed}, "
                            f"that is {pet_age} years old."
                        )

            print()

    finally:
        connection.close()


if __name__ == "__main__":
    main()

