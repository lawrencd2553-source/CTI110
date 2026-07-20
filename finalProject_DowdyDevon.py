 # Devon Dowdy
 # Date 07/18/2026
 # finalProject
 # Text-based adventure game



import random




import time


# -----------------------------
# PLAYER AND INVENTORY
# -----------------------------

player = {
    "name": "",
    "health": 100,
    "gold": 0,
    "level": 1,
    "xp": 0,
    "location": "Village",
    "weapon": "Wooden Sword"
}


inventory = {
    "Potion": 1,
    "Key": 0,
    "Magic Staff": 0,
    "Unicorn Horn": 0
}


# -----------------------------
# INTRO
# -----------------------------

def intro():

    print("🏰 THE LOST TREASURE ADVENTURE 🏰")

    player["name"] = input("Enter your name: ")

    print(f"\nWelcome {player['name']}!")
    print("Find treasure, collect items,")
    print("and defeat enemies to become a hero!")

    time.sleep(2)



# -----------------------------
# SHOW STATS
# -----------------------------

def show_stats(plzayer, inventory):

    print("\n--------- STATS ---------")
    print("Name:", player["name"])
    print("Health:", player["health"])
    print("Gold:", player["gold"])
    print("Level:", player["level"])
    print("XP:", player["xp"])
    print("Location:", player["location"])
    print("Weapon:", player["weapon"])

    print("\nInventory:")

    for item in inventory:
        print(item, ":", inventory[item])

    print("-------------------------")



# -----------------------------
# LEVEL UP
# -----------------------------

def level_up():

    if player["xp"] >= 50:

        player["level"] += 1
        player["xp"] = 0

        print("\n⭐ LEVEL UP!")
        print("You are now level", player["level"])



# -----------------------------
# BATTLE
# -----------------------------

def battle():

    enemy_health = random.randint(20,40)

    print("\n👹 A monster appears!")

    while enemy_health > 0:

        print("\nMonster HP:", enemy_health)
        print("Your HP:", player["health"])

        print("1. Attack")
        print("2. Run")

        choice = input("Choose: ")

        if choice == "1":

            damage = random.randint(5,15)

            if player["weapon"] == "Magic Staff":
                damage += 10

            print("You dealt", damage, "damage!")

            enemy_health -= damage


            if enemy_health > 0:

                damage = random.randint(5,10)

                player["health"] -= damage

                print("Monster hit you for", damage)


        elif choice == "2":

            print("You escaped!")

            return


    print("\n🎉 You defeated the monster!")

    player["gold"] += 20
    player["xp"] += 25

    level_up()



# -----------------------------
# UNICORN EVENT
# -----------------------------

def unicorn():

    print("\n🦄 A rare unicorn appears!")

    choice = input("Approach unicorn? (yes/no): ")

    if choice.lower() == "yes":

        reward = random.randint(1,3)

        if reward == 1:

            print("The unicorn heals you!")

            player["health"] = 100


        elif reward == 2:

            print("The unicorn gives you a magic horn!")

            inventory["Unicorn Horn"] = 1


        else:

            print("The unicorn gives you 50 gold!")

            player["gold"] += 50



# -----------------------------
# EXPLORE
# -----------------------------

def explore():

    locations = [
        "Forest",
        "Cave",
        "Castle"
    ]

    place = random.choice(locations)

    player["location"] = place

    print("\nYou travel to the", place)

    time.sleep(1)


    event = random.randint(1,4)


    if event == 1:

        battle()


    elif event == 2:

        gold = random.randint(10,30)

        print("You found", gold, "gold!")

        player["gold"] += gold


    elif event == 3:

        unicorn()


    else:

        print("You found a potion!")

        inventory["Potion"] += 1




# -----------------------------
# SIDE QUEST
# -----------------------------

def quest():

    print("\n🐶 A villager needs help finding a lost pet.")

    answer = input("Help them? (yes/no): ")

    if answer.lower() == "yes":

        print("Searching...")

        time.sleep(2)

        if random.randint(1,2) == 1:

            print("You found the pet!")

            print("You earned 30 gold.")

            player["gold"] += 30

        else:

            print("You couldn't find it.")




# -----------------------------
# USE ITEMS
# -----------------------------

def use_item():

    if inventory["Potion"] > 0:

        inventory["Potion"] -= 1

        player["health"] += 25

        if player["health"] > 100:
            player["health"] = 100

        print("You used a potion!")

    else:

        print("No potions available.")



# -----------------------------
# SHOP
# -----------------------------

def shop():

    print("\n🏪 Shop")

    print("Magic Staff - 50 gold")

    choice = input("Buy Magic Staff? (yes/no): ")


    if choice.lower() == "yes":

        if player["gold"] >= 50:

            player["gold"] -= 50

            inventory["Magic Staff"] = 1

            player["weapon"] = "Magic Staff"

            print("You bought a Magic Staff!")

        else:

            print("Not enough gold.")



# -----------------------------
# MAIN GAME
# -----------------------------

def main():

    intro()

    playing = True


    while playing:

        print("\n===== MENU =====")
        print("1. Explore")
        print("2. View Stats")
        print("3. Use Potion")
        print("4. Side Quest")
        print("5. Shop")
        print("6. Quit")


        choice = input("Choose: ")


        if choice == "1":

            explore()


        elif choice == "2":

            show_stats(player, inventory)


        elif choice == "3":

            use_item()


        elif choice == "4":

            quest()


        elif choice == "5":

            shop()


        elif choice == "6":

            print("Thanks for playing!")

            playing = False


        else:

            print("Invalid choice.")


        if player["health"] <= 0:

            print("💀 Game Over!")

            playing = False



# START GAME

main()
