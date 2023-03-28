a = int(input("Введите число A: "))
b = int(input("Введите число B: "))


def a_power_b(a,b):
    if b == 1:
        return a
    else:
        return a*a_power_b(a,b-1)
    
print(a_power_b(a,b))
     


