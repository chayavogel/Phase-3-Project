# Phase 3 CLI + ORM Project
## Solar System Explorer

## Description

This is a command line interface (CLI) application that allows users to explore the one-to-many relationship of planets and their multiple moons. It can easily be adapted to represent many other one-to-many relationships.

---

## Visuals
This is an image of the full menu:

![Alt text](<Screenshot 2023-12-22 at 11.28.35 AM.png>)

---

## Usage

Fork the Repository:
Fork the repository on GitHub.

Clone the forked repository to your local machine:
Command: `git clone git@github.com:chayavogel/Phase-3-Project.git`

Navigate to the Project Directory:
Command: `cd Phase-3-Project`

Install Dependencies:
Create a virtual environment and install the project dependencies.
Command: `pipenv install`

Activate the Virtual Environment:
Command: `pipenv shell`

Run the CLI Application:
Command: `python my_cli_app.py`

You may now navigate the menu!

---

## The File Structure and Contents

.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   └── moon.py
    │   └── planet.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
    └── seed.py

## cli.py

This Command Line Interface (CLI) application allows users to explore information about planets and moons in our solar system with leveled menus. Most of the actions will call methods that will modify instances of the moon and planet classes, as well as ORM methods to modify the database.

### Available Commands

#### Main Menu

- **Option 0:** Exit the program.
- **Option 1:** Explore information about planets.
- **Option 2:** Explore information about moons.

#### Planets Menu

- **Option 0:** Exit to the main menu.
- **Option 1:** List all planets.
- **Option 2:** Find a planet by name.
- **Option 3:** Create a new planet.
- **Option 4:** Update information about a planet.
- **Option 5:** Delete a planet.
- **Option 6:** List all moons of a specific planet.

#### Moons Menu

- **Option 0:** Exit to the main menu.
- **Option 1:** List all moons.
- **Option 2:** Find a moon by name.
- **Option 3:** Create a new moon.
- **Option 4:** Update information about a moon.
- **Option 5:** Delete a moon.
- **Option 6:** Display the parent planet of a moon.

### Usage

To select an option, enter a number corresponding to the action you'd like to carry out and follow the prompts. 

### Additional Notes

- Each action corresponds to a specific function in the `helpers.py` file, making the code modular.
- The program runs indefinitely until the user chooses to exit.
- Proper error handling is implemented to guide users in case of invalid choices.

## planet.py

The Planet class is designed to represent individual planets in the solar system with associated attributes and provides methods for managing and interacting with planet instances. These methods are called in the `helpers.py` file.

### Instance Attributes

- `id`: An integer representing the unique identifier of the planet.
- `name`: A string representing the name of the planet.
- `color`: A string representing the color of the planet.

### Class Methods

1. `create_table`

Allows you to initially create a database table to store planet information if it hasn't been created yet.

`drop_table`

Allows you to delete the database table used for storing planet information.

3. `save`

Allows you to save a newly created planet instance to the database. The instance is added to the planets table.

4. `create`

Creates a new planet instance with the provided name and color. This instance is stored in the `all` class attribute.

5. `update`

Allows you to update the information of a planet both in its object and in the database.

6. `delete`

Allows you to delete a planet instance and remove its corresponding row from the database.

7. `instance_from_db`

Creates a planet instance from a database row. Used to convert database query results into Planet objects.

8. `get_all`

Retrieves all planet instances from the database and returns a list of Planet objects.

9. `find_by_id`

Finds a planet instance by its ID and returns the corresponding Planet object.

10. `find_by_name`

Finds a planet instance by its name and returns the corresponding Planet object.

11. `moons`

Retrieves all moons associated with the planet.

## moon.py

The Moon class is designed to represent individual moons with associated attributes and provides methods for managing and interacting with moon instances. These methods are called in the `helpers.py` file.

### Instance Attributes

- `id`: An integer representing the unique identifier of the planet.
- `name`: A string representing the name of the moon.
- `planet_id`: An integer representing the ID of the parent planet. It serves as a reference to an instance of the Planet class.

### Class Methods

1. `create_table`

Allows you to initially create a database table to store moon information if it hasn't been created yet.

2. `drop_table`

Allows you to delete the database table used for storing moon information.

3. `create`

Creates a new moon instance with the provided name and planet_id. This instance is stored in the `all` class attribute.

4. `instance_from_db`

Creates a moon instance from a database row. Used to convert database query results into Moon objects.

5. `get_all`

Retrieves all moon instances from the database and returns a list of Moon objects.

6. `find_by_id`

Finds a moon instance by its ID and returns the corresponding Moon object.

7. `find_by_name`

Finds a moon instance by its name and returns the corresponding Moon object.

### Instance Methods

1. `save`

Allows you to save a newly created moon instance to the database. The instance is added to the moons table.

2. `update`

Allows you to update the information of a moon both in its object and in the database.

3. `delete`

Allows you to delete a moon instance and remove its corresponding row from the database.

## helpers.py

Each of the helper methods are called when its corresponding option on the menu is selected.

## seed.py

There is some optional seed data to get you started with two planets and some of their moons.

### Usage

Run python lib/seed.py to create the data. You should see the words "seeded database" printed to the terminal. 
