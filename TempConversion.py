#converting celcius to farenheit

celcius=float(input("Enter temp in celcius :\n"))
faren= (celcius* 9/5)+32
print (f" {celcius} in farenheit = ", faren)

faren= float(input("Enter temp in faren : \n"))
celcius= (5/9)* (faren-32)
print(f" {faren} in celcius = {celcius}")