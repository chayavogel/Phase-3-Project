#/Users/chayavogel/Documents/Solar-System-Explorer/src/cli.py
# note to self - reduce repetitive code

from data_helpers import (
    exit_program,
    list_planets,
    find_planet_by_name,
    create_planet,
    update_planet,
    delete_planet,
    list_moons,
    find_moon_by_name,
    create_moon,
    update_moon,
    delete_moon,
    list_planet_moons,
    display_moon_planet
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
    print("------------THE SOLAR SYSTEM-------------")
    print("----------------MAIN MENU----------------")
    print("Please select an option by entering one of the numbers below, and then pressing the Enter key:")
    print("0. Exit the program")
    print("1. Planets Menu")
    print("2. Moons Menu")

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
            create_planet()

        elif planet_choice == "4":
            update_planet()

        elif planet_choice == "5":
            delete_planet()

        elif planet_choice == "6":
            list_planet_moons()

        else:
            print("Invalid choice")

def planets_menu():
    # Display the planets menu options to the user.
    print("--------------------------------------------")
    print("----------------PLANETS MENU----------------")
    print("Please select an option by entering one of the numbers below:")
    print("0. Exit to main menu")
    print("1. List all planets")
    print("2. Find planet by name")
    print("3. Create planet")
    print("4. Update planet")
    print("5. Delete planet and its moons")
    print("6. List all moons of a planet")

def moons():
    while True:
        moons_menu()
        moon_choice = input("> ")

        if moon_choice == "0":
            break

        elif moon_choice == "1":
            list_moons()

        elif moon_choice == "2":
            find_moon_by_name()

        elif moon_choice == "3":
            create_moon()

        elif moon_choice == "4":
            update_moon()

        elif moon_choice == "5":
            delete_moon()

        elif moon_choice == "6":
            display_moon_planet()

        else:
            print("Invalid choice")

def moons_menu():
    print("------------------------------------------")
    print("----------------MOONS MENU----------------")
    print("Please select an option by entering one of the numbers below:")
    print("0. Exit to main menu")
    print("1. List all moons")
    print("2. Find moon by name")
    print("3. Create moon")
    print("4. Update moon")
    print("5. Delete moon")
    print("6. Display parent planet of a moon")

if __name__ == "__main__":
    main()
