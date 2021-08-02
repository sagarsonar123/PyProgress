#reverse
def reverse(string):
    new=""
    n=len(string)
    for i in range (n):
        a=string[n-1-i]
        new=new+a
    print(new)
reverse('sagar')        