# code for Q7 June 2011 CS Paper 1 AQA

names = ["Ben", "Thor", "Zoe", "Kate"]
current = 0
found = False
playerName = input("which player are you looking for?")
while found == False and current+1 <= len(names):
    if names[current] == playerName:
        found = True
    else:
        current += 1
if found == True:
    print("Yes, they do have a top score")
else:
    print("No, they do not have a top score")

