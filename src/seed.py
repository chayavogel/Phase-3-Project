#!/usr/bin/env python3

#/Users/chayavogel/Documents/Solar-System-Explorer/src/seed.py

from models.planet import Planet
from models.moon import Moon

def seed_database():
    Moon.drop_table()
    Planet.drop_table()
    Planet.create_table()
    Moon.create_table()

    mercury = Planet.create("Mercury", "Grayish")
    venus = Planet.create("Venus", "Yellowish")
    earth = Planet.create("Earth", "Blue and green")
    mars = Planet.create("Mars", "Reddish")
    jupiter = Planet.create("Jupiter", "Orange and brown striped")
    saturn = Planet.create("Saturn", "Pale yellow")
    uranus = Planet.create("Uranus", "Light blue")
    neptune = Planet.create("Neptune", "Dark blue")

    Moon.create("Luna", earth.id)
    Moon.create("Phobos", mars.id)
    Moon.create("Deimos", mars.id)
    Moon.create("Titan", saturn.id)
    Moon.create("Enceladus", saturn.id)
    Moon.create("Ganymede", jupiter.id)
    Moon.create("Europa", jupiter.id)

if __name__ == "__main__":
    seed_database()
    print("Seeded database")
