# input integer number from user
n = input("Enter a positive integer number: ")

# iteration/loop will start from 2 because 0 and 1 is known prime number
for i in range(2, int(n)):
    # `isPrime` is a flag or we can say it a boolean variable which will represent or will be `False` if we found it composite number
    isPrime = True
    # max range is i/2 because there is no need to check if number/2 is less for e.g 50 / 2 = 25 and 25 * 2 = 50 and 26 * 2 = 52 so every number will be exceeding, it will be a waste of loop
    for number in range(2, int(i/2)):
        if i % number == 0:
            isPrime = False
            break
    if isPrime:
        print(i, " is a prime number")
    else:
        print(i, " is not a prime number")
    