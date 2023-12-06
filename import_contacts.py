def import_contacts():
    import os
    
    text_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    print("\nВ текущей директории находятся следующие текстовые файлы:\n")
    for nn, f in enumerate(text_files, 1):
        print(f"\t{nn}. [{f}]\n")
    choosen_file_index = int(input('\nВведите номер файла в списке: '))-1
    
    print(f"\nВыбран файл {text_files[choosen_file_index]} .\n")
    
    with open(text_files[choosen_file_index], 'r', encoding='utf-8') as import_from:
        contacts_to_import = import_from.read().rstrip().split('\n\n')
    
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        existing_contacts = file.read().rstrip().split('\n\n')
                
    count = 0
        
    with open('phonebook.txt', 'a', encoding='utf-8') as file:    
        for contact in contacts_to_import:
            if contact not in existing_contacts:
                file.write(contact + "\n" + "\n")
                count += 1
                
    print(f'\n Добавлено {count} контактов.\n')