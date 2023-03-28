a=2
b=2

def sum_ret (a, b):
    if b==1:
        return a+1
    else:
        return(sum_ret(a, b-1)+1)

print(sum_ret (a, b))