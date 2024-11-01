#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.planet import Planet
from models.moon import Moon

def seed_database():
    Moon.drop_table()
    Planet.drop_table()
    Planet.create_table()
    Moon.create_table()

    saturn = Planet.create("Saturn", "Pale yellow")
    mars = Planet.create(
        "Mars", "Reddish")
    Moon.create("Phobos", mars.id)
    Moon.create("Deimos", mars.id)
    Moon.create("Titan", saturn.id)
    Moon.create("Enceladus", saturn.id)
    Moon.create("Mimas", saturn.id)

if __name__ == "__main__":
    seed_database()
    print("Seeded database")