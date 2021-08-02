#finding the greatest of three numbers

num1= int(input("Please enter first number"))
num2=int(input("please enter second number"))
num3=int(input("Please enter third number"))
if num1<num2:
    if num3<num2:
        print(f" {num2} is greatest ")
    else:
        print(f"{num3} is greatest ")
elif num3<num1:
    print(f"{num1} is greatest")