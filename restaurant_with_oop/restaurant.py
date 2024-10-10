class Restaurant:
    def __init__(self, name):
        self.name = name
        self.chef = None
        self.server = None
        self.manager = None
        self.menu = []
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
            self.revenue += amount
            self.balance += order.bill
            customer.due_amount = 0
            return amount - order.bill

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