#0112358 fibonacci series
n=int(input("Enter n"))
a=0
b=1
sum=0
count=0
while count<n:
    print(sum, end="")
    count+=1
    a=b
    b=sum
    sum=a+b
    