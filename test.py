x=input("r")
a=int(x)
def sum_func(n):
    s=0
    for y in range(1,n+1):
        s=s+a**y
    return s
b=input("till what haang")
n=int(b)
print(sum_func(n))