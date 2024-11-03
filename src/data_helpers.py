from models.planet import Planet
from models.moon import Moon

def exit_program():
    print("Goodbye!")
    exit()

def list_planets():
    planets = Planet.get_all()
    for i, planet in enumerate(planets, start=1):
        print(f"{i}) {planet.name}: color = {planet.color}")

def find_planet_by_name():
    name = input("Enter the planet's name: ")
    planet = Planet.find_by_name(name)
    if planet:
        print(f"{planet.name}: color = {planet.color}")
    else:
        print("\033[91mERROR: Planet {name} not found. (Note: planets are case-sensitive)\033[0m")

def create_planet():
    name = input("Enter the planet's name (correctly spelled and in title case): ")
    color = input("Enter the planet's color: ")
    try:
        planet = Planet.create(name, color)
        print(f'Success! {planet.name}: color = {planet.color}')
    except Exception as exc:
        print("\033[91mERROR creating planet: \033[0m", exc)

def update_planet():
    name = input("Enter the planet's name: ")
    if planet := Planet.find_by_name(name):
        try:
            print(f"Current data => {planet.name}: color = {planet.color}")
            new_name = input("Enter the planet's new name (correctly spelled and in title case): ")
            new_color = input("Enter the planet's new color: ")
            planet.name = new_name
            planet.color = new_color
            planet.update()
            print(f'Success! {planet.name}: color = {planet.color}')
        except Exception as exc:
            print("\033[91mERROR updating planet: \033[0m", exc)
    else:
        print("\033[91mERROR: Planet {name} not found\033[0m")

def delete_planet():
    name = input("Enter the planet's name: ")
    if planet := Planet.find_by_name(name):
        planet.delete()
        print(f'Planet {name} and its moons deleted')
    else:
        print("\033[91mERROR: Planet {name} not found. (Note: planets are case-sensitive)\033[0m")

def list_planet_moons():
    name = input("Enter planet's name: ")
    planet = Planet.find_by_name(name)
    if planet:
        moons = planet.moons()
        if not moons:
            print("This planet has no moons!")
        else:
            for i, moon in enumerate(moons, start=1):
                print(f"{i}) {moon.name}")
    else: 
        print("\033[91mERROR: Planet {name} not found. (Note: planets are case-sensitive)\033[0m")

def list_moons():
    moons = Moon.get_all()
    for i, moon in enumerate(moons, start=1):
        parent_planet = Planet.find_by_id(moon.planet_id)
        print(f"{i}) {moon.name}: Parent planet = {parent_planet.name}")

def find_moon_by_name():
    name = input("Enter a moon's name: ")
    moon = Moon.find_by_name(name)
    if moon:
        parent_planet = Planet.find_by_id(moon.planet_id)
        print(f"{moon.name}: Parent planet = {parent_planet.name}")
    else: 
        print("\033[91mERROR: Moon {name} not found. (Note: moons are case-sensitive)\033[0m")

def create_moon():
    name = input("Enter the moon's name: ")
    parent_planet_input = input("Enter the moon's parent planet (correctly spelled, title case): ")
    parent_planet_match = Planet.find_by_name(parent_planet_input)
    if parent_planet_match:
        try:
            moon = Moon.create(name, parent_planet_match.id)
            print(f'Success! {moon.name}: Parent Planet = {parent_planet_match.name}')
        except Exception as exc:
            print("\033[91mERROR creating moon: \033[0m", exc)
    else:
        print("\033[91mERROR: Parent planet {parent_planet_input} not found. Parent planet must exist before the creation of a moon. (Note: planets are case-sensitive)\033[0m")

def update_moon():
    name = input("Enter the moon's current name: ")
    if moon := Moon.find_by_name(name):
        try:
            current_parent_planet = Planet.find_by_id(moon.planet_id)
            print(f"Current data: {moon.name}: Parent Planet = {current_parent_planet.name}")
            new_name = input("Enter moon's new name (title-case): ")
            moon.name = new_name
            new_planet_name = input("Enter moon's new parent-planet (correctly spelled and in title case): ")
            if new_planet_object := Planet.find_by_name(new_planet_name):
                moon.planet_id = new_planet_object.id
                moon.update()
                print(f"Success! {moon.name}: Parent Planet = {new_planet_object.name}")
            else:
                print("\033[91mPlanet {new_planet_name} not found\033[0m")
        except Exception as exc:
            print("\033[91mERROR updating moon: \033[0m", exc)
    else: 
        print("\033[91mERROR: Moon {name} not found. (Note: moons are case-sensitive)\033[0m")

def delete_moon():
    name = input("Enter the moon's name: ")
    moon = Moon.find_by_name(name)
    if moon:
        try:
            moon.delete()
            print(f"Moon {name} deleted!")
        except Exception as exc:
            print("\033[91mERROR deleting moon: \033[0m", exc)
    else: 
        print("\033[91mMoon {name} not found. (Note: Moons are case-sensitive)\033[0m")

def display_moon_planet():
    name = input("Enter the moon's name: ")
    if moon := Moon.find_by_name(name):
        parent_planet = Planet.find_by_id(moon.planet_id)
        print(f"Parent planet: {parent_planet.name}")
        return parent_planet.name
    else: 
        print("\033[91mMoon {name} not found. (Note: Moons are case-sensitive)\033[0m")
