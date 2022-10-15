#ASSIGN GRADES ACCORDING  TO MARKS
marks=int(input("enter your mark:"))
if marks<=100 and marks>90:
    print("Your grade is A")
elif marks<=90 and marks>80 :
    print("your grade is B")
elif marks<=80 and marks>70:
    print("Your grade is c")
elif marks<=0 and marks>0:
    print("Your grade is D")
else:
    print("invalid")
