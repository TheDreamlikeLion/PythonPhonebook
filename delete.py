def delete_contact():
    print(
        'Возможные варианты поиска:\n'
        '1. по фамилии\n'
        '2. по имени\n'
        '3. по отчеству\n'
        '4. по номеру\n'
        '5. по городу\n'
    )

    index_var = int(input('Введите вариант поиска: '))-1
    to_delete_index_set = set()
    
    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_str = file.read()
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    for str_index in range(0, len(contacts_list)):
        contact_list = contacts_list[str_index].replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'Найдено упоминание "{contact_list[index_var]}" в контакте:\n{contacts_list[str_index]}\n')
            print()
            user_choice = input("Хотите безвозвратно УДАЛИТЬ эту запись? (Да/Нет)")
            if user_choice in ("Д", "д", "Да", "да"):
                if index_var in (0, 1, 2, 3, 4):
                    to_delete_index_set.add(str_index)
                    print('\nДанный контакт будет удален!\n')
                else:
                    print("\nНекорректный ввод!\n")

            else:
                print("Этот контакт не будет удалён. \n")

    if len(to_delete_index_set) > 0:
        user_choice = input(f"Подтвердите удаление записей (кол-во запсией - {len(to_delete_index_set)}). (Да/Нет)")
        if user_choice in ("Д", "д", "Да", "да"):
            with open('phonebook.txt', 'w+', encoding='utf-8') as file:
                for str_index in range(0, len(contacts_list)):
                    if str_index not in to_delete_index_set:
                        file.write(contacts_list[str_index] + "\n" + "\n")
                print("\nКонтакты в файле обновлены.\n")
    
        print('\nКонтакты не были изменены.\n')