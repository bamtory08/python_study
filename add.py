import random

def yay():
    a=random.randint(1, 40)
    b=random.randint(1, 20)
    op=random.randint(1, 3)

    q=str(a)

    if op == 1:
        q=q+"+"
    if op == 2:
        q=q+"-"
    if op == 3:
        q=q+"*"

    q=q+str(b)

    return q
s1=0
s2=0

for x in range(5):
    q=yay()
    print(q)
    a=input("=")
    b=int(a)

    if eval(q)==b:
        s1=s1+1
        print("dang u good bro")
    else:
        s2=s2+1
        print("no bro")

print ("yea:", s1, "nah:", s2)
if s2==0:
    print("respect")
if s1==0:
    print("study math")
    