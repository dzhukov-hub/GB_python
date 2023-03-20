word = input("Введите слово буквами: ")


p1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T',
      'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
p2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
p3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
p4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
p5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
p8 = ['J', 'X', 'Ш', 'Э', 'Ю']
p10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

cost = 0

for i in (word.upper()):
    if i in p1:
        cost += 1
    if i in p2:
        cost += 2
    if i in p3:
        cost += 3
    if i in p4:
        cost += 4
    if i in p5:
        cost += 5
    if i in p8:
        cost += 10


print(cost)
