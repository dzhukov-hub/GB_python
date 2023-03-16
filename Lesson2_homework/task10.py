from random import randint
coins_num = int(input("Введите количество монет: "))
heads_num = 0
tails_num = 0

for i in range(coins_num):
    if randint(0, 1) == 0:
        heads_num += 1
    else:
        tails_num += 1
print(f'Кол-во монет стороной "орел":  {heads_num}')
print(f'Кол-во монет стороной "решка": {tails_num}')

if heads_num < tails_num:
    print(f"Минимальное число монеток, которое нужно перевернуть: {heads_num}")
else:
    print(f"Минимальное число монеток, которое нужно перевернуть: {tails_num}")


# # coins_n
# for i in range(1,  10):
#     print(f"i-{i}")
#     print(randint(1, coins_num))
