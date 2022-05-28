# program code from CS paper 1 June 2017

plain = input("What is your plaintext?")
RLE = ""
count = 1
for position in range(len(plain)):
    if position+1 == len(plain):
        RLE = RLE + plain[position]
        RLE = RLE + str(count)
    elif plain[position] != plain[position+1]:
        RLE = RLE + plain[position]
        RLE = RLE + str(count)
        count = 1
    else:
        count += 1
print(RLE)



