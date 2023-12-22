# lib/models/planet.py
from models.__init__ import CURSOR, CONN

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

    all = {}

    def __init__(self, name, color, id=None):
        self.id = id
        self.name = name
        self.color = color
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError(
                "Name must be a string"
            )
        elif not name in PLANETS:
            raise ValueError(
                "Name must be a correctly-spelled and title-cased planet in the Solar System"
            )
        else: 
            self._name = name

        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if isinstance(color, str) and 1 <= len(color):
            self._color = color
        else: 
            raise ValueError(
                "Color must be a non-empty string"
            )
        
    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS planets (
            id INTEGER PRIMARY KEY,
            name TEXT,
            color TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):

        sql = """
            DROP TABLE IF EXISTS planets;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):

        sql = """
            INSERT INTO planets (name, color)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.color))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, color):

        planet = cls(name, color)
        planet.save()
        return planet
    
    def update(self):

        sql = """
            UPDATE planets
            SET name = ?, color = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.color, self.id))
        CONN.commit()
    
    def delete(self):

        sql = """
            DELETE FROM planets
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):

        planet = cls.all.get(row[0])
        if planet:
            planet.name = row[1]
            planet.color = row[2]
        else:
            planet = cls(row[1], row[2])
            planet.id = row[0]
            cls.all[planet.id] = planet
        return planet
    
    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM planets
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT *
            FROM planets
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):

        sql = """
            SELECT *
            FROM planets
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def moons(self):

        from models.moon import Moon
        sql = """
            SELECT * FROM moons
            WHERE planet_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Moon.instance_from_db(row) for row in rows
        ]