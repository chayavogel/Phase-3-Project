# /Users/chayavogel/Documents/Solar-System-Explorer/src/models/planet.py

from . import CURSOR, CONN

# List of valid planets in the Solar System
PLANETS = [
    "Mercury", 
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune"
]

class Planet:

    # Planet instances dictionary
    all = {}

    def __init__(self, name, color, id=None):
        self.id = id
        self.name = name
        self.color = color

    # Property and setter for name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        elif name not in PLANETS:
            raise ValueError("Planet must be a member of the Solar System, in title-case, and correctly spelled.")
        else: 
            self._name = name

    # Property and setter for color
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if isinstance(color, str) and len(color) >= 1:
            self._color = color
        else: 
            raise ValueError("Color must be a non-empty string")

    # Class method to create the planets table if it doesn't already exist
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS planets (
                id INTEGER PRIMARY KEY,
                name TEXT,
                color TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    # Class method to delete the planets table
    @classmethod
    def drop_table(cls):
        sql = "DROP TABLE IF EXISTS planets;"
        CURSOR.execute(sql)
        CONN.commit()

    # Save the current Planet instance to the database and add it to the `all` dictionary in the class object
    def save(self):
        sql = "INSERT INTO planets (name, color) VALUES (?, ?)"
        CURSOR.execute(sql, (self.name, self.color))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    # Class method to create and save a new Planet instance in one step
    @classmethod
    def create(cls, name, color):
        planet = cls(name, color)
        planet.save()
        return planet

    # Update the existing Planet instance in the database with new data
    def update(self):
        sql = "UPDATE planets SET name = ?, color = ? WHERE id = ?"
        CURSOR.execute(sql, (self.name, self.color, self.id))
        CONN.commit()

    # Delete the Planet instance and its related moons from the database
    def delete(self):
        planet_sql = "DELETE FROM planets WHERE id = ?"
        moons_sql = "DELETE FROM moons WHERE planet_id = ?"

        try:
            CURSOR.execute(moons_sql, (self.id,))
            CURSOR.execute(planet_sql, (self.id,))
            CONN.commit()
            del type(self).all[self.id]
            self.id = None
        except Exception as exc:
            print("Error deleting planet and moons:", exc)

    # Create an instance of Planet from a database row
    @classmethod
    def instance_from_db(cls, row):
        planet = cls.all.get(row[0])
        if planet:
            planet.name = row[1]
            planet.color = row[2]
        else:
            planet = cls(row[1], row[2], id=row[0])
            cls.all[planet.id] = planet
        return planet

    # Retrieve all planets from the database
    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM planets"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    # Find a planet by its ID
    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM planets WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    # Find a planet by its name
    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM planets WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    # Retrieve all moons associated with the planet
    def moons(self):
        from models.moon import Moon
        sql = "SELECT * FROM moons WHERE planet_id = ?"
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Moon.instance_from_db(row) for row in rows]