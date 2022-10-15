#TAKE THREE USER INPUT AND CHECK IS IT A TRIANGLE OR NOT
a=int(input("enter first side:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a+b>c and a+c>b and b+c>a:
    print("it can form a triangle")
else:
    print("can not form a triangle")