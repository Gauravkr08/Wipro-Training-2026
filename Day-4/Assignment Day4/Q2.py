'''
Create a class BankAccount that:

1. Uses a parameterized constructor to initialize account_number and balance

2. Implements methods deposit(amount) and withdraw(amount)

3. Uses a destructor to display a message when the object is deleted

4. Handle invalid withdrawal using proper checks
'''


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print(f"Account {self.account_number} created with balance {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")

    def __del__(self):
        print(f"BankAccount {self.account_number} is being deleted.")


account1 = BankAccount(12345, 1000)

account1.deposit(500)
account1.withdraw(300)
account1.withdraw(2000)

del account1