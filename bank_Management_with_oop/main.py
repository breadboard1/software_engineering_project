from bank import Bank
from user import User, Admin

def main():
    grameen = Bank('Grameen Bank', 'Baridhara')
    # banglalink = Bank('Banglalink Bank', 'Borguna')

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
    baker.deposit(1000, grameen)
    baker.withdraw(300, grameen)
    baker.deposit(200, grameen)
    # baker.check_balance()
    baker.withdraw(1000, grameen)

    # grameen.loan_feature_management(younus_sir)

    baker.take_loan(1000, grameen)
    baker.take_loan(1000, grameen)
    baker.take_loan(1000, grameen)
    baker.check_balance()

    # rosul = User('Rahat ali', 'rahat@gmail.com', 'kokrol', 'savings')
    # banglalink.add_admin(younus_sir)
    # banglalink.add_user(rosul)

    baker.transfer_money(100, nusrat, grameen)
    baker.check_balance()

    nusrat.check_balance()

    baker.transaction_history()
    nusrat.transaction_history()

    grameen.loan_amount(younus_sir)
    grameen.total_balance(younus_sir)


if __name__ == "__main__":
    main()