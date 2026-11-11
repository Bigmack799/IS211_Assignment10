# IS211_Assignment10

**What is the purpose of the `person_pet` table?**

The purpose of the `person_pet` table is to establish a relationship between the `person` and `pet` tables within the database. It serves as a junction table that connects each person's unique ID to the ID of their associated pets. This allows the database to represent a many-to-many relationship, meaning one person can own multiple pets, and a pet can potentially be associated with multiple people.

For example, James Smith has a person ID of 1 and is associated with Rusty and Bella, whose pet IDs are 1 and 2. Rather than storing the person's information repeatedly for each pet, the `person_pet` table maintains these connections using their IDs. This approach reduces unnecessary data duplication, improves database organization, and makes retrieving information through SQL queries more efficient.

IS211_Assignment10
