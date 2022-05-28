# code for unkown past paper AQA CS paper 1 
howFar = int(input("how far to count?"))
while howFar < 1:
    howFar = int(input("not a valid number, please try again."))
for myLoop in range(1,howFar):
    if myLoop%3==0 and myLoop%5==0:
        print("FizzBuzz")
    elif myLoop%3==0:
        print("Fizz")
    elif myLoop%5==0:
        print("Buzz")
    else:
        print(myLoop)