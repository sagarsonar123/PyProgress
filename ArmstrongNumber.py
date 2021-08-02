def armstrong(x):
    sum=0
    print("Your number is ")
    x=str(x)
    n=len(x)
    print ("power = " ,n)
    for i in range (n):
        new=(pow(int(x[i]),n))
        sum=sum+new
        print(sum)
    x=int(x)
    if x==sum:
        print ("Entered number is an armstrong number")
    else:
        print("number is not an armstrong number")
    
