def bubbleSort(arr):
    n=len(arr)
    print(n)
    for i in range (n-1):
        for j in range (n-i-1):
            if arr[j+1]<arr[j]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
array=[1,2,7,3,5,8,2,0]
bubbleSort(array)
print(array)