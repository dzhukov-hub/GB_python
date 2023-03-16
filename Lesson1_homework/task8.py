m, n = int(input("Введите размер шоколадки - число n: ")), int(input("Введите размер шоколадки - число m: "))
k = int(input("Введите кол-во долек - число k: "))

# m = 3
# n = 5
# k = 6


if k < m*n and (k % m == 0 or k % n == 0):
    print("yes")
else:
    print("no")
