import os
import shutil
import sys
from Functions.victory_Function import victory
from Functions.Bank_account_Function import bank_account
from Functions.folders_and_files import output_folders_and_files
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
    print('11.Выход')


    choice = input('Выберете пункт меню:')

    if choice == '1':
        name = input('Введите название папки:')
        os.mkdir(name)
    elif choice == '2':
        name = input('Введите название папки:')
        os.rmdir(name)
    elif choice == '3':
        original_file = input('Введите название файла для копирования')
        target_file = input('Введите новое название файла')
        shutil.copy(original_file, target_file)
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':

        text_dir = output_folders_and_files(os.path.isdir,[])
        print(text_dir)
    elif choice == '6':

        text = output_folders_and_files(os.path.isfile,[])
        print(text)
    elif choice == '7':
        print(sys.platform)
    elif choice == '8':
        print('Создатель программы: Wolf2747')
    elif choice == '9':
        victory()
    elif choice == '10':
        bank_account()
    elif choice == '11':
        break
    else:
        print('неверный пункт')
