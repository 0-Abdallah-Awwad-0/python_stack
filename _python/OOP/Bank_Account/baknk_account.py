class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


# Account 1
account1 = BankAccount(0.02, 100)

account1.deposit(50).deposit(100).deposit(200).withdraw(80).yield_interest().display_account_info()


# Account 2
account2 = BankAccount(0.03, 200)

account2.deposit(100).deposit(50).withdraw(100).withdraw(50).withdraw(300).withdraw(50).yield_interest().display_account_info()