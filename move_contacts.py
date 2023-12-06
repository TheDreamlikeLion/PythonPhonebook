def move_contacts():
    import os
    
    text_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    print("\nВ текущей директории находятся следующие текстовые файлы:\n")
    for nn, f in enumerate(text_files, 1):
        print(f"\t{nn}. [{f}]\n")
    choosen_from_file_index = int(input('\nВведите номер файла, ИЗ КОТОРОГО надо перенести контакт:'))-1
    choosen_to_file_index = int(input('\nВведите номер файла, В КОТОРЫЙ надо перенести контакт:'))-1
    print('\n')
    print(f"\nВы хотите перенести контакт из файла {text_files[choosen_from_file_index]} в файл {text_files[choosen_to_file_index]}.\n")
    
    with open(text_files[choosen_from_file_index], 'r', encoding='utf-8') as import_from:
        existing_contacts = import_from.read().rstrip().split('\n\n')
    
    with open(text_files[choosen_to_file_index], 'r', encoding='utf-8') as import_to:
        import_to_contacts = import_to.read().rstrip().split('\n\n')

    print(
        'Необходимо найти контакт для переноса.\n'
        '\n'
        'Возможные варианты поиска:\n'
        '1. по фамилии\n'
        '2. по имени\n'
        '3. по отчеству\n'
        '4. по номеру\n'
        '5. по городу\n'
    )

    index_var = int(input('Введите вариант поиска: '))-1
    index_to_move = None    
    search = input('Введите данные для поиска: ')

    for str_index in range(0, len(existing_contacts)):
        contact_list = existing_contacts[str_index].replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'Найдено упоминание "{contact_list[index_var]}" в контакте:\n{existing_contacts[str_index]}\n')
            print()
            user_choice = input(f"Хотите перенести этот контакт в файл {text_files[choosen_to_file_index]}? (Да/Нет)")
            if user_choice in ("Д", "д", "Да", "да"):
                if index_var in (0, 1, 2, 3, 4):
                    index_to_move = str_index
                    movement_fact = True
                    print('\n')
                else:
                    print("\nНекорректный ввод!\n")

            else:
                print("Этот контакт не будет перенесён. \n")

    if movement_fact:
        if existing_contacts[index_to_move] not in import_to_contacts:
            with open(text_files[choosen_to_file_index], 'a+', encoding='utf-8') as import_to:
                import_to.write(existing_contacts[index_to_move] + "\n" + "\n")
            
            print('\nДанный контакт был перенесен!\n')
            
            with open(text_files[choosen_from_file_index], 'w', encoding='utf-8') as import_from:
                for str_index in range(0, len(existing_contacts)):
                    if str_index != index_to_move:
                        import_from.write(existing_contacts[str_index] + "\n" + "\n")
            
            print("Контакты в файлах обновлены.\n")
        else:
            print(f"\nТакой контакт уже есть в файле {text_files[choosen_to_file_index]} .\n")
    else:
        print('\nКонтакты не были изменены.\n')