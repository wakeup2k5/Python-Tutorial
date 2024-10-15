# Write a program to print all the prime numbers between 2 and a number (N) given by the user.

def checkIfPrime(number):
    isPrime = True
    for index in range(2, number - 1):
        if number % index == 0:
            isPrime = False
            break
    return isPrime

maxNumber = int(input("Please enter a maximum number for the sequence of prime numbers: "))

for index in range(2, maxNumber):
    if checkIfPrime(index):
        print(index)

if checkIfPrime(maxNumber):
    print(maxNumber)