import view
from classes import PhoneBook
import socket

if socket.gethostname()=='DZHUKOV-NB':
    file_path='C:\python\GB\phone_book.txt'
else:
    file_path='phone_book.txt'


def show_menu():
    phonebook = PhoneBook()
    while True:
        command = view.phone_book_menu()
        match command:
            case 1:
                ph=phonebook.show_phone_book(file_path)
                view.print_phone_book(ph)
            case 2:
                phonebook.input_new_row(file_path)
                ph=phonebook.show_phone_book(file_path)
                view.print_phone_book(ph)
            case 3:
                phonebook.delete_row(file_path)
                ph=phonebook.show_phone_book(file_path)
                view.print_phone_book(ph)
            case 4:
                phonebook.update_row(file_path)
                ph=phonebook.show_phone_book(file_path)
                view.print_phone_book(ph)
            case 5:
                break