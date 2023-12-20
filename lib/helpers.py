# lib/helpers.py
from models.planet import Planet
from models.moon import Moon

def exit_program():
    print("Goodbye!")
    exit()

def list_planets():

    planets = Planet.get_all()

    for i, planet in enumerate(planets, start = 1):
        print(i, planet)

def find_planet_by_name():

    name = input("Enter the department's name: ")
    planet = Planet.find_by_name(name)
    print(planet) if planet else print(
        f'Planet {name} not found')

def find_planet_by_id():

    id_ = input("Enter the planets's id: ")
    planet = Planet.find_by_id(id_)
    print(planet) if planet else print(f'Planet {id_} not found')


def create_planet():
    name = input("Enter the planets's name (in title_case, with correct spelling): ")
    color = input("Enter the planets's color: ")
    try:
        planet = Planet.create(name, color)
        print(f'Success: {planet}')
    except Exception as exc:
        print("Error creating planet: ", exc)


def update_planet():
    id_ = input("Enter the planet's id: ")
    if planet := Planet.find_by_id(id_):
        try:
            print(f"Current data: {planet}")
            name = input("Enter the planet's new name (title-case, correct spelling): ")
            planet.name = name
            color = input("Enter the planet's new color: ")
            planet.color = color

            planet.update()
            print(f'Success: {planet}')
        except Exception as exc:
            print("Error updating planet: ", exc)
    else:
        print(f'Planet {id_} not found')


def delete_planet():
    id_ = input("Enter the planet's id: ")
    if planet := Planet.find_by_id(id_):
        planet.delete()
        print(f'Planet {id_} deleted')
    else:
        print(f'Planet {id_} not found')

def list_moons():
    moons = Moon.get_all()
    for i, moon in enumerate(moons, start = 1):
        print(i, moon)

def find_moon_by_name():
    name = input("Enter a moon's name {title-case}: ")
    moon = Moon.find_by_name(name)
    if moon:
        print(moon)
    else: 
        print(f"Moon {name} not found")

def find_moon_by_id():
    id_ = input("Enter a moon's id: ")
    moon = Moon.find_by_id(id_)
    if moon:
        print(moon)
    else: 
        print(f"Moon {id_} not found")


def create_moon():
    name = input("Enter moon name (title-case): ")
    planet = int(input("Enter mooon's parent-planet id: "))
    try:
        moon = Moon.create(name, planet)
        print(f"Success {moon}")
    except Exception as exc:
        print(f"Error creating moon ", exc)

def update_moon():
    id_ = input("Enter moon's id: ")
    moon = Moon.find_by_id(id_)
    if moon:
        try:
            print(f"Current data: {moon}")
            name = input("Enter moon's new name (title-case): ")
            moon.name = name
            planet = int(input("Enter moon's new parent-planet id: "))
            moon.planet_id = planet
            moon.update()
            print(f"Success {moon}")
        except Exception as exc:
            print(f"Error updating moon ", exc)
    else: 
        print("Moon {id_} not found")

def delete_moon():
    id_ = input("Enter moon's id: ")
    moon = Moon.find_by_id(id_)
    if moon:
        try:
            moon.delete()
            print(f"Moon {id_} deleted!")
        except Exception as exc:
            print(f"Error deleting moon ", exc)
    else: 
        print(f"Moon {id_} not found")


def list_planet_moons():
    id_ = input("Enter planet's id: ")
    planet = Planet.find_by_id(id_)
    if planet:
        moons = planet.moons()
        if not len(moons):
            print("This planet has no moons!")
        for i, moon in enumerate(moons, start = 1):
            print(i, moon)
    else: 
        print(f"Planet {id_} not found")