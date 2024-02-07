def factorial(n):
    fact=1
    for x in range(1, n+1):
        fact=fact*x
    return fact
def cccc(y, z):
    t=y-z
    w=factorial(y)/factorial(t)/factorial(z)
    return w

print("yCz")
a=input("y=")
y=int(a)
c=input("z=")
z=int(c)


print(y, "C", z, "=", cccc(y, z))