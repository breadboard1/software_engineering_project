class Person:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

class User(Person):
    def __init__(self, name, email, address, account_type):
        super().__init__(name, email, address)
        self.account_type = account_type
        self.__balance = 0
        self.account_no = f"{self.name}-{self.email}"
        self.transections = []

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Your current balance is {self.__balance}.")
            self.transections.append(f"Successful Deposit of {amount} taka.")
        else:
            print("Not enough money.")
            self.transections.append(f"unsuccessful deposit attempt of {amount} taka.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Current balance {self.__balance}. Withdrawal {amount}.")
            self.transections.append(f"Successful withdrawal of {amount} taka.")
        else:
            print("Not enough money to withdraw.")
            self.transections.append(f"unsuccessful withdrawal attempt of {amount} taka.")

    def check_balance(self):
        print(f"Your current balance is {self.__balance}.")

    def transection_hostory(self):
        for transection in self.transections:
            print(transection)

    def take_loan(self, amount):
        pass

    def transfer_money(self, user, amount):
        pass


class Admin(Person):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)



