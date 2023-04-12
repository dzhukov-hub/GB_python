import socket 
phone_book=[]
import text_constant

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

def input_new_row():
        with open(file_path, "a", encoding='utf-8-sig') as phone_book_file:
            last_name=input(text_constant.input_last_name)
            phone_book_file.write(f"\n{last_name},")
            first_name=input(text_constant.input_first_name)
            phone_book_file.write(f"{first_name},")
            phone_number=input(text_constant.input_phone_number)
            phone_book_file.write(f"{phone_number},")
            comment=input(text_constant.input_comment)
            phone_book_file.write(f"{comment}")
            phone_book_file.close()
            show_phone_book()

def delete_row():
    last_name_delete=input(text_constant.delete_row_caption)
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


def update_row():
    last_name_updated = input(text_constant.update_row_caption)
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