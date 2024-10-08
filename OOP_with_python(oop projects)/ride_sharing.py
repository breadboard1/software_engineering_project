from abc import ABC, abstractmethod
from datetime import datetime

class RideSharingCompany:
    def __init__(self, company_name):
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_driver(self, driver):
        self.drivers.append(driver)

    def __repr__(self):
        return f'.....Welcome to {self.company_name}.....'

class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.__nid = nid
        self.id = 0
        self.__wallet = 0

    @abstractmethod
    def profile(self):
        raise NotImplementedError

class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        self.__wallet = initial_amount
        self.current_location = current_location
        self.current_ride = None
        super().__init__(name, email, nid)

    def profile(self):
        print(f"Hi, I am {self.name}. This is my email {self.email} ID.")

    def load_cash(self, amount):
        if amount > 0:
            self.__wallet += amount

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self):
        pass

    def show_current_ride(self):
        print(f"Current ride {self.current_ride}.")

class Driver(User):
    def __init__(self, name, email, nid, current_location):
        self.current_location = current_location
        self.__wallet = 0
        super().__init__(name, email, nid)

    def profile(self):
        print(f"Hi, I am {self.name}. This is my email {self.email} ID.")

    def accept_ride(self, ride):
        pass







# ubar = RideSharingCompany("ubar")
# ubar.add_driver("Rahim")
# ubar.add_driver("Karim")
# ubar.add_driver("Baker")
# moti = Rider("moti", "moti@goti.com", "12345", "bikrompur", 1000)

# for driver in ubar.drivers:
#     print(driver)

