def bank_account():
    money = 0
    history = []

    def pay(money):
        coast = int(input('Введите сумму покупки:'))
        if coast > money:
            print('Недостаточно средств')
        else:
            money -= coast
            buy = input('Введите название покупки')
            history.append((buy, coast))
        return money

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print('Ваш счет:', money)

        choice = input('Выберите пункт меню')

        if choice == '1':
            money += int(input('Сколько средств вы хотите внести?:'))
        elif choice == '2':
            money = pay(money)
        elif choice == '3':
            print(history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
