class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__bank_balance = 0
        self.admins = []
        self.users = []
        self.__total_loan = 0
        self.loan = True
        self.maxLoan = 50000
        self.minLoan = 500

    def balance(self, amount, type):
        if type == 'deposit':
            self.__bank_balance += amount
        elif type == 'withdraw':
            self.__bank_balance -= amount
        else:
            print("Error!")

    def adjust_loan(self, amount, type):
        if type == 'withdraw':
            self.__total_loan += amount
        else:
            self.__total_loan -= amount

    def dewlia(self, amount):
        return amount > self.__bank_balance

    def loan_true_false(self):
        return self.loan

    def add_user(self, user):
        self.users.append(user)

    def add_admin(self, admin):
        self.admins.append(admin)

    def __repr__(self):
        for user in self.users:
            print(user.name)
        return ""

    def delete_user(self, admin, user):
        if admin in self.admins:
            if user in self.users:
                self.users.remove(user)
                print("Deleted Successfully...")
            else:
                print("User not found!")
        else:
            print("You are not an admin.")

    def show_all_user(self, admin):
        if admin in self.admins:
            print("---------All Users-------")
            for user in self.users:
                print(f"Name : {user.name}, Account No : {user.account_no}")
            print("---------------------------")
        else:
            print("You are not an admin.")

    def total_balance(self, admin):
        if admin in self.admins:
            print(f"Total {self.name} balance is {self.__bank_balance} taka.")
        else:
            print("Sorry! You need administrative power...")

    def loan_amount(self, admin):
        if admin in self.admins:
            print(f"Total loan amount {self.__total_loan} taka.")
        else:
            print("You need administrative power...")

    def loan_feature_management(self, admin):
        if admin in self.admins:
            self.loan ^= 1
        else:
            print("You need administrative power...")