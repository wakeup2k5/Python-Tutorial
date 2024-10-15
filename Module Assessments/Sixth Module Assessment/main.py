# Write a program that calculates the factorial of a number given by the user, then prints the output.

number = int(input("Please enter a number to calculate its factorial: "))

factorial = number
number = number - 1

if number > 0:
    while number > 0:
        factorial *= number
        number -= 1
else:
    factorial = 1
    
print(f"The factorial is {factorial}")