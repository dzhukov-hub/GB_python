from random import randint

n = int(input("Введите натуральное число N: "))
a = [int(input(f"Введите {_+1}-й элемент списка: ")) for _ in range(n)]
x = int(input("Введите натуральное число X: "))

a_val = a[0]
abs_delta = abs(a[0]-x)

for i in range(n):
    if abs(a[i]-x) < abs_delta:
        abs_delta = abs(a[i]-x)
        a_val = a[i]


print(a_val)
