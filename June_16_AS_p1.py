# code for paper 1 AS June 2016 AQA
value = int(input("Enter integer (0-99):"))
operation = input("Calculate additive or multiplicative persistance? (a or m)?")
count = 0
while value > 9:
    if operation == "a":
        value = (value//10) + (value%10)
    else:
        value = (value//10) * (value%10)
    count += 1
print("the persistence is:")
print(count)

"""
inputs:  expected outputs:   result:
87,a     2                   PASS
39,m     3                   PASS

"""