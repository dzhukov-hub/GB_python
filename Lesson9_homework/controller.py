import view
from modul import show_phone_book, input_new_row, delete_row, update_row

def show_menu():
    while True:
        command = view.phone_book_menu()
        #print(command)
        match command:
            case 1:
                show_phone_book()
            case 2:
                input_new_row()
            case 3:
                delete_row()
            case 4:
                update_row()
            case 5:
                break
        
    