import random

k = 2
my_list = [random.randint(1, 100) for i in range(10)]
my_list_shift = [-1 for i in range(10)]

print((my_list))


for i in range(10):
    if i+k <= len(my_list)-1:
        j = i+k
    else:
        j = i+k-len(my_list)
    my_list_shift[j] = my_list[i]

#print(my_list_shift)
#print(my_list[:k])
#print(my_list[:-k])

#print(my_list[k:])
#print(my_list[-k:])

print(my_list[-1])