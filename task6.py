ticket_num = int(input("Введите номер билета: "))


left_num = ticket_num//1000
right_num = ticket_num % 1000


if (left_num // 100+left_num//10 % 10+left_num % 10) == (right_num // 100+right_num//10 % 10+right_num % 10):
    print("yes")
else:
    print("no")
