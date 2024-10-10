class Restaurant:
    def __init__(self, name, rent, menu=[]):
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.rent = rent
        self.menu = []
        self.orders = []
        self.revenue = 0
        self.profit = 0
        self.expense = 0
        self.balance = 0

    def add_employee(self, employee_type, employee):
        if employee_type == 'chef':
            self.chef = employee
        elif employee_type == 'server':
            self.server = employee
        elif employee_type == 'manager':
            self.manager = employee

    def receive_payment(self, order, amount, customer):
        if order.bill <= amount:
            self.revenue += order.bill
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill
        else:
            print(f"Not enough money...")

    def pay_expense(self, amount, description):
        if amount < self.balance:
            self.expense += amount
            self.balance -= amount
            print(f"Expense for {description}")
        else:
            print("Not enough money to pay{amount}")

    def pay_salary(self, employee):
        if employee.salary < self.balance:
            employee.receive_salary()

    def add_order(self, order):
        self.orders.append(order)


    def show_employee(self):
        print(f"---------SHOWING EMPLOYEES-----------")
        if self.chef is not None:
            print(f"chef : {self.chef.name} with salary {self.chef.salary}.")
        if self.server is not None:
            print(f"server : {self.server.name} with salary {self.server.salary}.")