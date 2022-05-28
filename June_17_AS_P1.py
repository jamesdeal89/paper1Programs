# program file from CS paper 1 June 2017 AS AQA

number1 = int(input("enter a whole number:"))
number2 = int(input("enter another whole number:"))
temp1 = number1
temp2 = number2
while temp1 != temp2:
    if temp1 > temp2:
        temp1 = temp1 - temp2
    else:
        temp2 = temp2 - temp1
result = temp1
print(result, " is GCF of ", number1, " and ", number2)

