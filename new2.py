#TAKE USER INPUT IF LENGTH OF INPUT STRING IS MORE THAN THREE CHARACTER THAN ADD ING AS SUFFIX TO IT
#  ELSE PRINT THE STRING AS IT IS
a=input("enter a string:")
b="ing"

if len(a)>3:
    print(a+b)
else:
    print(a)