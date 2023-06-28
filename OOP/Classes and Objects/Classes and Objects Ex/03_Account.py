class Account:
    def __init__(self, id_number, name, balance=0):
        self.id = id_number
        self.name = name
        self.balance = balance

    def return_balance(self):
        return self.balance

    def credit(self, amount):
        self.balance += amount
        return self.return_balance()

    def debit(self, amount):
        if amount > self.balance:
            return "Amount exceeded balance"

        self.balance -= amount
        return self.return_balance()

    def info(self):
        return f"User {self.name} with account {self.id} has {self.balance} balance"


account1 = Account(1234, "George", 1000)
print(account1.credit(500))
print(account1.debit(1500))
print(account1.info())

account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())
