class BankOperation:
    def __init__(self, name, Id):
        self.name = name
        self.Id = Id
        self.balance = 0

    def deposit(self, amount):
        # Add code to deposit money
        self.balance += amount

    def withdraw(self, amount):
        # Add code to withdraw money
        if amount > self.balance:
            print("Insufficient funds")
        else: 
            self.balance -= amount


if "__name__" == "__main__":
    access = BankOperation("Access Bank", 123456)
    access.deposit(1000)
    access.withdraw(500)
    print(access.balance)



