#armstrong without using inbuilt function

def armstrongOrNot(num):
    temp=num
    print(temp)
    add=0
    count=0
    while(num):
        x=num%10
        num=num//10
        count=count+1
    print ("power is ",count)
    num=temp
    while(num):
        x=num%10
        add=add+(pow(x,count))
        num=num//10
    if (add==temp):
        print("the number is an armstrong number !")
    else:
        print("number is not an armstrong number !")