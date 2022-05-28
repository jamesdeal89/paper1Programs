# code for Q16 paper 1 AQA CS June 2021 

answer = 0
column = 8
while column >= 1:
    bit = int(input("enter bit value:"))
    answer = answer + (column*bit)
    column = column/2
print("decimal value is:", answer)