PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

num_pennies = int(input("Enter number of pennies: "))
num_nickels = int(input("Enter number of nickels: "))
num_dimes = int(input("Enter number of dimes: "))
num_quarters = int(input("Enter number of quarters: "))

total_cents = (num_pennies * PENNY_VALUE) + (num_nickels * NICKEL_VALUE) + (num_dimes * DIME_VALUE) + (num_quarters * QUARTER_VALUE)

total_dollars = total_cents / PENNIES_IN_DOLLAR

if total_dollars == 1.0:
    print("Congratulations!")
    print("The amount you entered was exactly one dollar!")
    print("You win the game!!")

elif total_dollars > 1.0:
    print("Sorry, the amount you entered was more than one dollar.")

else:
    print("Sorry, the amount you entered was less than one dollar.")