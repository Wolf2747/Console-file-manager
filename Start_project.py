import os

while True:
    print('1.Создание папки')
    print('2.Удалить (файл/папку)')
    print('3.Копировать (файл/папку)')
    print('4.Просмотр содержимого рабочей директории')
    print('5.Посмотреть только папки')
    print('6.Посмотреть только файлы')
    print('7.Просмотр информации об операционной системе')
    print('8.Создатель программы')
    print('9.Играть в викторину')
    print('10.Мой Банковский счет')
    print('11.Смена рабочей дериктории')
    print('12.Выход')

    choice = input('Выберете пункт меню:')

    if choice == '1':
        name = input('Введите название папки:')
        os.mkdir(name)
    elif choice == '2':
        name = input('Введите название папки:')
        os.rmdir(name)
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        pass
    elif choice == '8':
        pass
    elif choice == '9':
        pass
    elif choice == '10':
        pass
    elif choice == '11':
        pass
    elif choice == '12':
        break
    else:
        print('неверный пункт')
