#print all prime numbers in range 1-100

upper=100
lower=1
for num in range (lower, upper+1):
       if num>1:
            for i in range (2, num):
                if (num%i) == 0:
                    break
            else:
                print (num)