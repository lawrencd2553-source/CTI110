# Devon Dowdy
# 07/18/2026
# P5Lab
# Self Checkout Change

import random

def disperse_change(change):

    cents = int(round(change * 100))
    dollars = cents // 100
    cents = cents % 100
    quarters = cents // 25
    cents = cents % 25
    dimes = cents // 10
    cents = cents % 10
    nickels = cents // 5
    cents = cents % 5
    pennies = cents

    if dollars > 0:
        print(f"${dollars} bills")
    if quarters > 0:
        print(f"{quarters} quarters")
    if dimes > 0:
        print(f"{dimes} dimes")
    if nickels > 0:
        print(f"{nickels} nickels")
    if pennies > 0:
        print(f"{pennies} pennies")

def main():
    customer_owes = round(random.uniform(1.00, 100.00), 2)
    print(f"Amount owed: ${customer_owes}")

    cash_paid = float(input("Enter cash paid: $"))

    change_owed = round(cash_paid - customer_owes, 2)
    print(f"Change owed: ${change_owed}")
    disperse_change(change_owed)

if __name__ == "__main__":
    main()
