import random

print("Welcome to Desi Dungeon: The Chai Quest")
name = input("Enter your name, brave explorer: ")

print("\nNamaste, " + name + "! You are in a dark underground station.")
print("Find the legendary Cutting Chai and escape... or be lost forever.\n")

health = 100
inventory = []

enemies = ["Bhoot Baba", "Annoying TC", "Wi-Fi Ghost", "Lost Passenger"]
items = ["Chai Token", "Power Bank", "Maggi", "Aadhaar Card"]

while health > 0:
    print("\nWhat do you want to do?")
    print("1. Explore area")
    print("2. Check inventory")
    print("3. Exit game")

    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        if random.randint(0, 1) == 0:
            enemy = random.choice(enemies)
            print("\nYou encountered " + enemy + "!")

            action = input("Do you want to [fight] or [run]? ").strip().lower()

            if action == "fight":
                if random.randint(0, 1) == 1:
                    print("You defeated " + enemy + " using your desi logic!")
                else:
                    damage = random.randint(10, 30)
                    health -= damage
                    print(enemy + " hit you!")
                    print("You lost", damage, "health.")
                    print("Health =", health)
            else:
                print("You ran away safely... but they might return.")

        else:
            item = random.choice(items)
            print("\nYou found a " + item + "!")
            inventory.append(item)

            if "Chai Token" in inventory:
                print("\nYou found the Chai Token!")
                print("The chaiwala appears out of nowhere!")
                print("You sip the Cutting Chai.")
                print("Congratulations! You won the game.")
                break

    elif choice == "2":
        print("\nInventory:", inventory)
        print("Health:", health)

    elif choice == "3":
        print("\nThanks for playing! Jai Hind!")
        break

    else:
        print("Invalid choice. Try again.")

if health <= 0:
    print("\nYou fainted in the desi dungeon.")
    print("Game Over.")