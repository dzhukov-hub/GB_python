def phone_book_menu() -> int:
    print('''
    Меню телефонного справочника:
    1. Показать телефонный справочник
    2. Ввести новую запись
    3. Удалить запись
    4. Обновить запись
    5. Выход''')
    command = ''
    while True:
        command=input("Введите номер желаемого действия: ")
        if command.isdigit and 0 <=int(command)<=5:
            return int(command)
        else:
            print(f"\nВведена неверная команда.\n")
            #print()
