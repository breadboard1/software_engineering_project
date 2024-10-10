from menu import Pizza, Burger, Drinks, Menu
from restaurant import Restaurant
from user import Chef, Manager, Customer, Server
from order import Order

def main():
    menu = Menu()
    pizza_1 = Pizza('shutki pizza', 500, 'large', ['shutki', 'onion'])
    menu.add_menu_item('pizza', pizza_1)
    pizza_2 = Pizza('alu vorta pizza', 400, 'large', ['alu', 'oil'])
    menu.add_menu_item('pizza', pizza_2)
    pizza_3 = Pizza('dal pizza', 250, 'large', ['dal', 'nanan dal'])
    menu.add_menu_item('pizza', pizza_3)

    burger_1 = Burger('naga burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_menu_item('burger', burger_1)
    burger_2 = Burger('beef burger', 1200, 'beef', ['goru', 'haddi'])
    menu.add_menu_item('burger', burger_2)

    coke = Drinks('Coke', 50, True)
    menu.add_menu_item('drink', coke)
    coffee = Drinks('motka', 100, False)
    menu.add_menu_item('drink', coffee)

    # showing the menu
    menu.show_menu()

    # make a restaurant
    restaurant = Restaurant('doyal baba restaurant', 1000, menu)

    # add employees
    manager = Manager('kala chan', '293818', 'kala@gmail.com', 'kala pur', 1500, 'jan 1 2023', 'core')
    restaurant.add_employee('manager', manager)
    chef = Chef('roustom baburchi', '9238829', 'rustom@gmail.com', 'rustom nogor', 2000, 'jan 5 2023', 'chef', 'shahi gosto')
    restaurant.add_employee('chef', chef)
    server = Server('chotu', '739392', 'chotu@nai.com', 'restaurant', 200, 'Feb 5 2020', 'server')
    restaurant.add_employee('server', server)

    # show employees
    restaurant.show_employee()


    # adding customer details
    customer_1 = Customer('dildar', '837191', 'dildar@gmail.com', 'bonani', 1000)

    # customer_1 placing an order
    order_1 = Order(customer_1, [pizza_3, coffee])
    customer_1.place_order(order_1)
    restaurant.add_order(order_1)

    # customer_1 paying for order_1
    restaurant.receive_payment(order_1, 1500, customer_1)

    print("first customer revenue and balance consequtively :", restaurant.revenue, restaurant.balance)

    # adding customer details
    customer_2 = Customer('chuppu', '837191', 'dildar@gmail.com', 'bonani', 1000)
    # customer_2 placing an order
    order_2 = Order(customer_2, [pizza_3, burger_1, coffee])
    customer_2.place_order(order_2)
    restaurant.add_order(order_2)

    # customer_2 paying for order_2
    restaurant.receive_payment(order_2, 2000, customer_2)

    print("second cusotmer revenue and balance consequtively :", restaurant.revenue, restaurant.balance)

    # pay rent
    restaurant.pay_expense(restaurant.rent, 'rent')
    print("after rent, revenue, balance and expense consequtively :", restaurant.revenue, restaurant.balance, restaurant.expense)

    # paying salary
    restaurant.pay_salary(server)
    print("after salary, revenue, balance and expense consequtively :", restaurant.revenue, restaurant.balance, restaurant.expense)



if __name__ == "__main__":
    main()