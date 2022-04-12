class bank_account:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def display(self):
        print("The account owner is: " + self.name)
        print("The current balance of account is:", end=" ")
        print(self.balance, end=" US Dollars" + "\n")

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


ac_1 = bank_account("Caleb")
ac_2 = bank_account("Enoch")


def bank_class():
    ac_1.deposit(500)
    ac_1.withdraw(250)
    ac_1.display()
    ac_2.deposit(1000)
    ac_2.withdraw(789)
    ac_2.display()


bank_class()
