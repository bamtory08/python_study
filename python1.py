x=input("공비")
a=int(x)
z=input("몇항까지의 합")
b=int(z)
s=0
for y in range(1,b+1):
    s=s+a**y
print("공비:", x, "합:", s) 