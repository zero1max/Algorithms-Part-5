class BankAccount:
    bank_users = 0

    def __init__(self, fullname, balance=0):
        self.fullname = fullname
        self.balance = balance
        BankAccount.bank_users += 1

    def deposit(self, amount):
        self.balance += amount
        print(f"old money {amount} -> balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"money:{amount} -> balance: {self.balance} ")
        else:
            print(f"sizda yetarli pul yo'q. siz {self.balance}")  # noqa

    @classmethod
    def get_users_accounts(cls):
        return f"Bank users: {cls.bank_users}"

    @staticmethod
    def investors(balance, rate):
        return balance * rate / 100

    def __str__(self):
        return f"Fullname: {self.fullname} Balance: {self.balance}"


# Hisoblar ochamiz # noqa
users1 = BankAccount("Firdavs", 500)
users2 = BankAccount("Jamol", 1000)
print(users1)
print(users2)
# users list

# Mablag' qo'shish va yechib olish # noqa
users1.deposit(400)
users2.withdraw(500)
# money

# bank all users get
print(BankAccount.get_users_accounts())

# Investor
investor = BankAccount.investors(1000, 5)
print(f"Foyiz: {investor}")
