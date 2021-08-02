#strong number

summation=0
n=int(input("Please enter a number :"))
tempp=n
while (n):
    i=1 #initialize here so that it resets for every digit in user entered-number
    fact=1 #initialize here so that it resets for every digit in user entered-number
    rem=n%10
    while(i<=rem):
        fact=fact*i
        i=i+1
    summation=summation+fact
    n=n//10
if (summation==tempp):
    print("It is a strong number")
else:
    print("It is not a strong number")