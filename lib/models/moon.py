# lib/models/moon.py
from models.__init__ import CURSOR, CONN
from models.planet import Planet

class Moon:
    
    all = {}

    def __init__(self, name, planet_id, id=None):
        self.id = id
        self.name = name
        self.planet_id = planet_id
    
    def __repr__(self):
        return (
            f"<Moon {self.id}: {self.name} || Parent Planet ID: {self.planet_id}>"
        )
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 9:
            self._name = name
        else: 
            raise ValueError(
                "Name must be a non-empty string and cannot have more than 9 letters"
            )
    
    @property
    def planet_id(self):
        return self._planet_id

    @planet_id.setter
    def planet_id(self, planet_id):
        if type(planet_id) is int and Planet.find_by_id(planet_id):
            self._planet_id = planet_id
        else:
            raise ValueError(
                "planet_id must reference a planet in the database"
                )

    @classmethod
    def create_table(cls):

        sql = """
            CREATE TABLE IF NOT EXISTS moons (
            id INTEGER PRIMARY KEY,
            name TEXT,
            planet_id INTEGER,
            FOREIGN KEY (planet_id) REFERENCES planets(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):

        sql = """
            DROP TABLE IF EXISTS moons;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):

        sql = """
                INSERT INTO moons (name, planet_id)
                VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.planet_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):

        sql = """
            UPDATE moons
            SET name = ?, planet_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.planet_id, self.id))
        CONN.commit()

    def delete(self):

        sql = """
            DELETE FROM moons
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, name, planet_id):

        moon = cls(name, planet_id)
        moon.save()
        return moon

    @classmethod
    def instance_from_db(cls, row):

        moon = cls.all.get(row[0])
        if moon:
            moon.name = row[1]
            moon.planet_id = row[2]
        else:
            moon = cls(row[1], row[2])
            moon.id = row[0]
            cls.all[moon.id] = moon
        return moon

    @classmethod
    def get_all(cls):

        sql = """
            SELECT *
            FROM moons
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT *
            FROM moons
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):

        sql = """
            SELECT *
            FROM moons
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None