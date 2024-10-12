from bank import Bank
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
        self.transactions = []
        self.loanCount = 0
        self.maxLoanCount = 2

    def deposit(self, amount, bank):
        if amount > 0:
            self.__balance += amount
            bank.balance(amount, 'deposit') # adding to bank
            print(f"Your current balance is {self.__balance}. After deposit of {amount} taka.")
            self.transactions.append(f"Successful Deposit of {amount} taka. Current balance is {self.__balance} taka.")
        else:
            print(f"You can not deposit {amount} taka.")
            self.transactions.append(f"unsuccessful deposit attempt of {amount} taka. Current balace is {self.__balance} taka.")

    def withdraw(self, amount, bank):
        if bank.dewlia(amount):
            print("Bank sorboshanto hoie jabe...")
        elif amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            bank.balance(amount, 'withdraw')   # subtracting from bank
            print(f"Current balance {self.__balance}. Withdrawal {amount}.")
            self.transactions.append(f"Successful withdrawal of {amount} taka. Current balance is {self.__balance} taka.")
        else:
            print(f"Not enough money to withdraw {amount} taka.")
            self.transactions.append(f"unsuccessful withdrawal attempt of {amount} taka. Current balance is {self.__balance} taka.")

    def check_balance(self):
        print(f"Your current balance is {self.__balance} taka.")

    def transaction_history(self):
        print("---------Transactions History--------")
        for transection in self.transactions:
            print(transection)
        print("----------finished----------")

    def take_loan(self, amount, bank):
        if self.loanCount >= 2:
            print(f"You have already taken loan 2 times. You can't take is again.")
        elif bank.loan_true_false():
            if bank.minLoan <= amount <= bank.maxLoan:
                self.__balance += amount
                self.loanCount += 1
                bank.adjust_loan(amount, 'withdraw')
                self.transactions.append(f"You have taken loan {amount} taka. Current balance {self.__balance} taka.")
            else:
                print(f"Minmum loan amount is {bank.minLoan} and Maximum loan amount is {bank.maxLoan}.")
        else:
            print(f"Sorry, {bank.name} does not offer loan facility.")

    def pay_loan(self, amount, bank):
        pass

    def transfer_money(self, user, amount):
        pass


class Admin(Person):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)



