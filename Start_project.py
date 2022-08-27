import os
import shutil
import sys
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
        original_file = input('Введите название файла для копирования')
        target_file = input('Введите новое название файла')
        shutil.copy(original_file, target_file)
    elif choice == '4':
        print(os.listdir())
    elif choice == '5':

        dirname = '/py. Проекты/Console-file-manager/'
        dirfiles = os.listdir(dirname)

        fullpaths = map(lambda name: os.path.join(name), dirfiles)

        dirs = []

        for file in fullpaths:
            if os.path.isdir(file):
                dirs.append(file)

        print(list(dirs))
    elif choice == '6':
        import os

        dirname = '/py. Проекты/Console-file-manager/'
        dirfiles = os.listdir(dirname)

        fullpaths = map(lambda name: os.path.join(name), dirfiles)

        files = []

        for file in fullpaths:

            if os.path.isfile(file):
                files.append(file)

        print((list(files)))

    elif choice == '7':
        print(sys.platform)
    elif choice == '8':
        print('Создатель программы: Wolf2747')
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
