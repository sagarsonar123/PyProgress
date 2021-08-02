#largestnumber in array which is not sorted
array=[1,2,7,4,6,8,10]
def largest(arr):
    n=len(arr)
    large=0
    for i in range (n):
        if large<arr[i]:
            secondlargest=large
            large=arr[i]
    print(large)
largest(array)