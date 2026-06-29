 # Devon Dowdy
 # Date 06/26/2026
 # P3LAB
 # Calculate the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money.

change = float(input("Enter an amount of money: $"))

# Convert to total cents as integer
total_cents = int(change * 100)

if total_cents == 0:
    print("No change is needed.")
else:
    # Calculate the number of each denomination
    dollars = total_cents // 100
    total_cents %= 100

    quarters = total_cents // 25
    total_cents %= 25

    dimes = total_cents // 10
    total_cents %= 10

    nickels = total_cents // 5
    total_cents %= 5

    pennies = total_cents

    # Display the results
    if dollars > 0:
        print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
    if quarters > 0:
        print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
    if dimes > 0:
        print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
    if nickels > 0:
        print(f"{nickels} Nickel{'s' if nickels > 1 else ''}")
    if pennies > 0:
        print(f"{pennies} Pennie{'s' if pennies > 1 else ''}")