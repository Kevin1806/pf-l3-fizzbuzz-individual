num = 1

for i in range (1000):
    
    if (num % 15 == 0):
        print ("Fizzbuzz")
        num += 1
    elif (num % 5 == 0):
        print("Buzz")
        num += 1
    elif (num % 3 == 0):
        print("Fizz")
        num += 1
    else:
        print(num)
        num+=1