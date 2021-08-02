#prime number (divisible by 1 and number itself)

num=int(input("Please enter a number"))
flag=False
if num >1 :
    for i in range (2, num):
        if num%i == 0:
            flag=True
            break
else:
    print("number is not prime")
if flag:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")
