# code for unkown paper date Q6 AQA CS paper 1
denary = int(input("please enter the denary value:"))
binary = []
while denary > 0:
    binary.append(denary%2)
    denary = denary//2
count=-1
binaryCor = []
for _ in binary:
    binaryCor.append(binary[count])
    count-=1
print(binaryCor)
