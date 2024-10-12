from bank import Bank
from user import User, Admin

def main():
    grameen = Bank('Grameen Bank', 'Baridhara')
    # create admins
    younus_sir = Admin('Dr. Younus', 'younus@yahoo.com', 'Bangladesh')
    grameen.add_admin(younus_sir)

    # create users
    baker = User('baker', 'baker@gmail.com', 'bonani', 'current')
    grameen.add_user(baker)

    nusrat = User('nusrat ali', 'nusrat@gmail.com', 'rampura', 'savings')
    grameen.add_user(nusrat)

    hasnat = User('hasnat jobbar', 'hasnat@gmail.com', 'kakrail', 'savings')
    grameen.add_user(hasnat)

    # grameen.show_all_user(younus_sir)
    # grameen.show_all_user(hasnat)
    # print(grameen)
    baker.deposit(1000)
    baker.withdraw(2000)


if __name__ == "__main__":
    main()