import socket

print("Введите номер желаемого действия:")
print("1. Показать телефонный справочник")
print("2. Ввести новую запись")
print("3. Удалить запись")
print("4. Обновить запись")
command = int(input())

if command not in range(1, 5):
    print("Введена неверная команда")
    exit()

if socket.gethostname()=='DZHUKOV-NB':
    file_path='C:\python\GB\phone_book.txt'
else:
    file_path='phone_book.txt'


def show_phone_book():
    print("\nТЕЛЕФОННЫЙ СПРАВОЧНИК\n")
    phone_book_file = open(file_path, 'r', encoding='utf-8-sig')
    phone_book_data = phone_book_file.readlines()
    phone_book_file.close()
    for row in phone_book_data:
        print(row)

if command==1:
    show_phone_book()

if command==2:
    with open(file_path, "a", encoding='utf-8-sig') as phone_book_file:
        last_name=input("Введите Фамилию: ")
        phone_book_file.write(f"\n{last_name},")
        first_name=input("Введите Имя: ")
        phone_book_file.write(f"{first_name},")
        phone_number=input("Введите номер телефона: ")
        phone_book_file.write(f"{phone_number},")
        comment=input("Введите комментарий: ")
        phone_book_file.write(f"{comment}")
        phone_book_file.close()
        show_phone_book()

if command==3:
    last_name_delete=input("Введите фамилию либо имя удаляемого абонента: ")
    with open(file_path, "r", encoding='utf-8-sig') as phone_book_file:
        phone_book_data = phone_book_file.readlines()
        phone_book_file.close()
    with open(file_path, "w", encoding='utf-8-sig') as phone_book_file:
        for row in phone_book_data:
            if row.find(last_name_delete)==-1:
                phone_book_file.write(row)
            else:
                print(f"\nСледующая запись была удалена: {row}")
    phone_book_file.close()
    show_phone_book()

if command==4:
    last_name_updated = input("Введите фамилию либо имя абонента для обновления его записи: ")
    if_find_last_name=False
    with open(file_path, "r", encoding='utf-8-sig') as phone_book_file:
        phone_book_data = phone_book_file.readlines()
        phone_book_file.close()
    with open(file_path, "w", encoding='utf-8-sig') as phone_book_file:
        for row in phone_book_data:
            if row.find(last_name_updated)!=-1:
                if_find_last_name=True
                print("Введите номер колонки для обновления:\n 1.Фамилия\n 2.Имя\n 3.Телефон\n 4.Комментарий\n")
                column_update=int(input())
                last_name=row.split(',')[0]
                first_name=row.split(',')[1]
                phone_number=row.split(',')[2]
                comment=row.split(',')[3]
                if column_update==1:
                    last_name=input('Введите новое значение колонки "Фамилия: "')
                if column_update==2:
                    first_name=input('Введите новое значение колонки "Имя: "')
                if column_update==3:
                    phone_number=input('Введите новое значение колонки "Телефон: "')
                if column_update==4:
                    comment=input('Введите новое значение колонки "Комментарий: "')
                phone_book_file.write(f"{last_name},")
                phone_book_file.write(f"{first_name},")
                phone_book_file.write(f"{phone_number},")
                phone_book_file.write(f"{comment}")
            else:
                phone_book_file.write(row)
    if not if_find_last_name:
        print(f"\nАбонент с данными фамилией и именем не найден! \n")
    phone_book_file.close()
    show_phone_book()

