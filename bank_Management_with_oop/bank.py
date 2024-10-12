class Bank:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.__balance = 0
        self.admins = []
        self.users = []
        self.__loan = 0
        self.loan_feature = True

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
            print(f"Total bank balance is {self.__balance}")
        else:
            print("Sorry! You need administrative power...")

    def loan_amount(self, admin):
        if admin in self.admins:
            print(f"Total loan amount {self.loan_amount}.")
        else:
            print("You need administrative power...")

    def loan_feature_management(self, admin):
        if admin in self.admins:
            self.loan_feature = False
        else:
            print("You need administrative power...")