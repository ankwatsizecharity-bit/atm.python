# ATM Program

# STEP 1: Set up variables
pin = 2020
balance = 1000000
attempts = 0


# STEP 2: Ask for the PIN
while attempts < 3:
    entered_pin = int(
        input("Enter PIN: "))

    if entered_pin == pin:
        print("login successful!")
        break
    else:
        attempts += 1
        print("Incorrect PIN.")
        print("You have", 3 - attempts, "tries left.")

# If the user fails all 3 attempts
if attempts == 3:
    print("Card blocked!")

else:
    # STEP 3: Show the continuous menu
    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        # STEP 4: Handling the choices

        if choice == '1':
            print("Your current balance is:", balance)

        elif choice == '2':
            # STEP 5: Deposit
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance += amount
                print("Deposit successful!")
                print("Your new balance is:", balance)
            else:
                print("Error: Deposit amount must be greater than zero.")

        elif choice == '3':
            # STEP 5: Withdrawal
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Error: Enter an amount greater than 0.")
            elif amount > balance:
                print("Error: You do not have enough money!")
            else:
                balance -= amount
                print("Cash dispensed:", amount)
                print("Your new balance is:", balance)

        elif choice == '4':
            print("Thank you, TILL NEXT TIME!")
            break

        else:
            print("Invalid choice! Please enter 1, 2 or 3.")