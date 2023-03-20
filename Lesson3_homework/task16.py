
n = int(input("Введите натуральное число N: "))
a = [int(input(f"Введите {_+1}-й элемент списка: ")) for _ in range(n)]
x = int(input("Введите натуральное число X: "))

# Вариант 1 решения задачи
cnt = 0
for _ in range(n):
    if a[_] == x:
        cnt += 1

print(cnt)


# Варивант 2 решения задачи
# print(a.count(x))
