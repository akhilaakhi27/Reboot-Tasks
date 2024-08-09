
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited {amount} \n New balance is {self.balance}.')
        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'Withdrew {amount}\n New balance is {self.balance}.')
        elif amount > self.balance:
            print('Insufficient funds.')
        else:
            print('Withdrawal amount must be positive.')

    def check_balance(self):
        print(f'The balance of {self.owner} is {self.balance}.')
        return self.balance

account = BankAccount('Akhila', 2000)
account.deposit(500)
account.withdraw(400)
account.check_balance()
