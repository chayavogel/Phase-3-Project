# lib/helpers.py
from models.planet import Planet
from models.moon import Moon


def exit_program():
    print("Goodbye!")
    exit()

def list_planets():

    planets = Planet.get_all()

    for i, planet in enumerate(planets, start = 1):
            print(f"{i}) {planet.name}: color = {planet.color}")


def find_planet_by_name():

    name = input("Enter the planet's name: ")

    planet = Planet.find_by_name(name)

    if planet:
        print(f"{planet.name}: color = {planet.color}")
    else:
        print(f"ERROR: Planet {name} not found. (Note: planets are case-sensitive)")


def create_planet():

    name = input("Enter the planet's name (correctly spelled and in title_case): ")
    color = input("Enter the planet's color: ")
    try:
        planet = Planet.create(name, color)
        print(f'Success! {planet.name}: color = {planet.color}')
    except Exception as exc:
        print("Error creating planet: ", exc)


def update_planet():

    name = input("Enter the planet's name: ")

    if planet := Planet.find_by_name(name):
        try:
            print(f"Current data => {planet.name}: color = {planet.color}")
            name = input("Enter the planet's new name (correctly spelled and in title_case): ")
            planet.name = name
            color = input("Enter the planet's new color: ")
            planet.color = color

            planet.update()
            print(f'Success! {planet.name}: color = {planet.color}')
        except Exception as exc:
            print("Error updating planet: ", exc)
    else:
        print(f"ERROR: Planet {name} not found")


def delete_planet():

    name = input("Enter the planet's name: ")

    if planet := Planet.find_by_name(name):
        planet.delete()
        print(f'Planet {name} and its moons deleted')
    else:
        print(f"ERROR: Planet {name} not found. (Note: planets are case-sensitive)")


def list_planet_moons():
    name = input("Enter planet's name: ")
    planet = Planet.find_by_name(name)
    if planet:
        moons = planet.moons()
        if not len(moons):
            print("This planet has no moons!")
        for i, moon in enumerate(moons, start = 1):
            print(f"{i}) {moon.name}")
    else: 
        print(f"ERROR: Planet {name} not found. (Note: planets are case-sensitive)")


def list_moons():
    moons = Moon.get_all()
    for i, moon in enumerate(moons, start = 1):
        parent_planet = Planet.find_by_id(moon.planet_id)
        print(f"{i}) {moon.name}: Parent planet = {parent_planet.name}")


def find_moon_by_name():
    name = input("Enter a moon's name: ")
    moon = Moon.find_by_name(name)
    if moon:
        parent_planet = Planet.find_by_id(moon.planet_id)
        print(f"{moon.name}: Parent planet = {parent_planet.name}")
    else: 
        print(f"ERROR: Moon {name} not found. (Note: planets are case-sensitive)")


def create_moon():
    name = input("Enter the moon's name: ")
    parent_planet_input = input("Enter the moon's parent planet (correctly spelled, title_case): ")

    parent_planet_match = Planet.find_by_name(parent_planet_input)

    if parent_planet_match and parent_planet_input in parent_planet_match.name:
        try:
            moon = Moon.create(name, parent_planet_match.id)
            print(f'Success! {moon.name}: Parent Planet = {parent_planet_match.name}')
        except Exception as exc:
            print("Error creating planet: ", exc)
    else:
        print(f"ERROR: Parent planet {name} not found. Parent planet must exist before the creation of a moon. (Note: planets are case-sensitive)")


def update_moon():
    name = input("Enter the moon's current name: ")
    
    if moon := Moon.find_by_name(name):
        try:
            current_parent_planet = Planet.find_by_id(moon.planet_id)

            print(f"Current data: {moon.name}: Parent Planet = {current_parent_planet.name}")

            new_name = input("Enter moon's new name (title-case): ")
            moon.name = new_name
            new_planet_name = input("Enter moon's new parent-planet (correctly spelled and in title_case): ")
            if new_planet_object := Planet.find_by_name(new_planet_name):
                moon.planet_id = new_planet_object.id
                moon.update()
                print(f"Success! {moon.name}: Parent Planet = {new_planet_object.name}")
            else:
                print(f"Planet {new_planet_name} not found")
            
        except Exception as exc:
            print(f"Error updating moon: ", exc)
    else: 
        print(f"ERROR: Parent planet {name} not found. Parent planet must exist before the creation of a moon. (Note: planets are case-sensitive)")


def delete_moon():
    name = input("Enter the moon's name: ")
    moon = Moon.find_by_name(name)

    if moon:
        try:
            moon.delete()
            print(f"Moon {name} deleted!")
        except Exception as exc:
            print(f"Error deleting moon: ", exc)
    else: 
        print(f"Moon {name} not found. (Note: Moons are case-sensitive)")

def display_moon_planet():
    name = input("Enter the moon's name: ")
    if moon := Moon.find_by_name(name):
        parent_planet = Planet.find_by_id(moon.planet_id)
        print(f"Parent planet: {parent_planet.name}")
        return parent_planet.name
    else: 
        print(f"Moon {name} not found. (Note: Moons are case-sensitive)") 