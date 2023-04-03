print("Введите первый элемент прогрессии: ")
a1=int(input())

print("Введите разницу прогрессии: ")
n=int(input())

print("Введите количество элементов прогрессии: ")
d=int(input())

#a1=2
#n=10
#d=3

#my_list=[]
my_list=[a1+i*d for i in range(10)]

print(my_list)

