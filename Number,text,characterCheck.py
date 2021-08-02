#to check whether entered text is number, alphabet or a special character

string=input("Enter a character")
if (string.isdigit()):
    print("It is a digit")
elif (string.isalpha()):
    print("It is an alphabet")
else:
    print("it is a special character")