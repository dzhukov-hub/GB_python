import random

my_list = [random.randint(1, 20) for i in range(10)]
min_number = int(input("Введите минимальное значение диапазона: "))
max_number = int(input("Введите максимальное значение диапазона: "))
print("Исходный массив:")
print(my_list)

for i in range(len(my_list)):
    if min_number <= my_list[i] <= max_number:
        print(i)