from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class Customer(User):
    def __init__(self, name, phone, email, address, money):
        self.wallet = money
        self.__order = None
        super().__init__(name, phone, email, address)

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        print(f"{self.name} placed an order.")

    def eat_food(self, order):
        print(f"{self.name} food items {order.items}")

    def pay_for_order(self, amount):
        pass

    def give_tips(self, tips_amount):
        pass

    def write_review(self, stars):
        pass


class Employee(User):
    def __init__(self, name, phone, email, address, salary, starting_date, department):
        self.salary = salary
        self.due = salary
        self.starting_date = starting_date
        self.department = department
        super().__init__(name, phone, email, address)

    def receive_salary(self):
        self.due = 0


class Chef(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department, cooking_item):
        self.cooking_item = cooking_item
        super().__init__(name, phone, email, address, salary, starting_date, department)


class Server(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department):
        self.tips_earnings = 0
        super().__init__(name, phone, email, address, salary, starting_date, department)

    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def serve_food(self, order):
        pass

    def receive_tips(self, amount):
        self.tips_earnings += amount


class Manager(Employee):
    def __init__(self, name, phone, email, address, salary, starting_date, department):
        super().__init__(name, phone, email, address, salary, starting_date, department)