#INPUT AGES OF THREE PEOPLE
age1 = int(input("enter first age:"))
age2 = int(input("enter second age:"))
age3 = int(input("enter third age: "))
#FIND WHO IS THE YOUNGEST AND OLDEST AMONG TWO
if age1>age2 and age1>age3 :
    print("age1 is oldest")
elif age2>age1 and age2>age3:
    print("age2 is oldest ")
else:
    print("age3 is oldest")
if age1<age2 and age1<age3:
    print("age1 is youngest")
elif age2<age1 and age2<age3 :
    print("age2 is youngest ")
else:
    print("age3 is youngest")