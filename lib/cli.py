from helpers import (
    exit_program,
    list_planets,
    find_planet_by_name,
    find_planet_by_id,
    create_planet,
    update_planet,
    delete_planet,
    list_moons,
    find_moon_by_name,
    find_moon_by_id,
    create_moon,
    update_moon,
    delete_moon,
    list_planet_moons
)

def main():
    while True:
        main_menu()
        main_choice = input("> ")

        if main_choice == "0":
            exit_program()

        elif main_choice == "1":
            planets()

        elif main_choice == "2":
            moons()

        else:
            print("Invalid choice")

def main_menu():
    print("----------------MAIN MENU----------------")
    print("THE SOLAR SYSTEM")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Planets")
    print("2. Moons")

def planets():
    while True:
        planets_menu()
        planet_choice = input("> ")

        if planet_choice == "0":
            break

        elif planet_choice == "1":
            list_planets()

        elif planet_choice == "2":
            find_planet_by_name()

        elif planet_choice == "3":
            find_planet_by_id()

        elif planet_choice == "4":
            create_planet()

        elif planet_choice == "5":
            update_planet()

        elif planet_choice == "6":
            delete_planet()

        elif planet_choice == "7":
            list_planet_moons()

        else:
            print("Invalid choice")

def planets_menu():
    print("----------------PLANETS MENU----------------")
    print("Please select an option:")
    print("0. Exit to main menu")
    print("1. List all planets")
    print("2. Find planet by name")
    print("3. Find planet by id")
    print("4. Create planet")
    print("5. Update planet")
    print("6. Delete planet")
    print("7. List all moons in a planet")

def moons():
    while True:
        moons_menu()
        moon_choice = input("> ")

        if moon_choice == "0":
            break  # Exit to main menu

        elif moon_choice == "1":
            list_moons()

        elif moon_choice == "2":
            find_moon_by_name()

        elif moon_choice == "3":
            find_moon_by_id()

        elif moon_choice == "4":
            create_moon()

        elif moon_choice == "5":
            update_moon()

        elif moon_choice == "6":
            delete_moon()

        elif moon_choice == "7":
            # List all moons in a planet
            list_planet_moons()

        else:
            print("Invalid choice")

def moons_menu():
    print("----------------MOONS MENU----------------")
    print("Please select an option:")
    print("0. Exit to main menu")
    print("1. List all moons")
    print("2. Find moon by name")
    print("3. Find moon by id")
    print("4. Create moon")
    print("5. Update moon")
    print("6. Delete moon")
    print("7. List all moons in a planet")

if __name__ == "__main__":
    main()
