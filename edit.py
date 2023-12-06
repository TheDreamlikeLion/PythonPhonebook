### ДЗ ###
# Дополнить телефонный справочник возможностью изменения
# и удаления данных(по выбору). Пользователь также может
# ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

def edit_contact():
    print(
        'Выберите объект для редактирования:\n'
        '1. фамилию\n'
        '2. именя\n'
        '3. отчество\n'
        '4. номер телефона\n'
        '5. город\n'
    )

    index_var = int(input('Введите вариант редактирования: '))-1

    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    for str_index in range(0, len(contacts_list)):
        contact_list = contacts_list[str_index].replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'Найдено упоминание "{contact_list[index_var]}" в контакте:\n{contacts_list[str_index]}\n')
            print()
            user_choice = input("Хотите изменить эту запись? (Да/Нет)")
            if user_choice in ("Д", "д", "Да", "да"):
                if index_var in (0, 1, 2, 3, 4):
                    contact_list[index_var] = input(f"Введите новые данные. (Текущее значение: {contact_list[index_var]} )\n")
                    print("\nОтредактированный контакт: \n")
                    contacts_list[str_index] = str(contact_list[0]) + " " + str(contact_list[1]) + " " + str(contact_list[2]) + " " + str(contact_list[3]) + "\n" + str(contact_list[4])
                    print(contacts_list[str_index])
                    print()
                else:
                    print("\nНекорректный ввод!\n")

            else:
                print("Вы отказались от редактирования данного контакта. \n")

    print(*contacts_list, sep="\n")
    with open('phonebook.txt', 'w+', encoding='utf-8') as file:
        for contact_str in contacts_list:
            file.write(contact_str + "\n" + "\n")
    print('\nКонтакты сохранены в файл!\n')