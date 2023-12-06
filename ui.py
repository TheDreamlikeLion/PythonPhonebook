from logger import *
from edit import *
from import_contacts import *
from move_contacts import *
from delete import *


def interface():
    with open('phonebook.txt', 'a'):
        pass

    user_input = None
    while user_input != '0':
        print(
            'Возможные варианты действия:\n'
            '1. Добавить контакт\n'
            '2. Вывод списка контактов\n'
            '3. Поиск контакта\n'
            '4. Редактировать контакт\n' 
            '5. Удалить контакт\n'
            '6. Импорт контактов\n'
            '7. Перенос контактов\n'
            "\n"
            '0. Выход из программы\n'
            "\n"
        )

        user_input = input('Введите вариант: ')

        while user_input not in ('1', '2', '3', '4', '5', '6', '7', '0'):
            print('Некорректный ввод.')
            user_input = input('Введите вариант: ')

        print()

        match user_input:
            case '1':
                write_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                edit_contact()
            case '5':
                delete_contact()
            case '6':
                import_contacts()
            case '7':
                move_contacts()


