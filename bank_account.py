

class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance if initial_balance >= 0 else 0.0

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print(f"Error: Deposit amount must be positive.")

    def withdraw(self, amount: float):
        if amount <= 0:
            print(f"Error: Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Error: Insufficient funds for withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}, Current Balance: ${self.balance:.2f}")
                                                                          
if __name__ == "__main__":
    print("--- Testing Account 1 (Alice): ---")
    account1 = BankAccount("Alice", 100.00)
    account1.deposit(50.00)
    account1.withdraw(30.00)
    account1.withdraw(200.00)
    account1.display_account_info()

    print("\n--- Testing Account 2 (Bob): ---")
    account2 = BankAccount("Bob")
    account2.deposit(-10.00)
    account2.deposit(75.00)
    account2.display_account_info()