# Write a program to print the Fibonacci sequence for a count given by the user.

quantityRequested = int(input("Please enter the number of fibonacci numbers to display: "))

num1 = 0
num2 = 1

count = 1

while count <= quantityRequested:
    if count == 1:
        print(0)
    else:
        nextNum = num1 + num2
        print(nextNum)
        num1 = num2
        num2 = nextNum
    count += 1