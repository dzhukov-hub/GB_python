input_number = int(input("Введите трхзначное число: "))


print("Сумма цифр трехзначного числа: "+str(input_number // 100+input_number//10 % 10+input_number % 10))
