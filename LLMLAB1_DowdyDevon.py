# Devon Dowdy
# 07/11/2026
# LLMLAB1
# USE AI to write code

import random
import string

# Dictionary to store generated passwords
passwords = {}

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def create_password():
    name = input("Enter a name for this password: ")

    if name in passwords:
        print("A password with that name already exists.")
        return

    length = int(input("Enter password length: "))

    password = generate_password(length)

    passwords[name] = {
        "password": password,
        "creation_date": "Generated",
        "strength": "Strong" if length >= 12 else "Moderate"
    }

    print("Password created successfully!")
    print("Password:", password)


def view_passwords():
    if len(passwords) == 0:
        print("No passwords saved.")
        return

    for name, info in passwords.items():
        print("\nName:", name)
        print("Password:", info["password"])
        print("Creation Date:", info["creation_date"])
        print("Strength:", info["strength"])


def delete_password():
    name = input("Enter the name of the password to delete: ")

    if name in passwords:
        del passwords[name]
        print("Password deleted.")
    else:
        print("Password not found.")


def menu():
    while True:
        print("\n===== Password Generator =====")
        print("1. Generate Password")
        print("2. View Saved Passwords")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            delete_password()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


menu()