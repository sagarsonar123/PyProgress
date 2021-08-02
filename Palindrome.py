def isPalindrome(string):
    stringlen=len(string)
    n=len(string)//2
    for i in range (n):
        if string[i]!=string[n-1-i]:
            print("Not palindrome")
            break
        else:
            print("Yes, string is a palindrome")
            break
isPalindrome('aaajaaa')