# Write a program that gets two inputs from the user
# and performs basic calculator functionalities on them 
# (add, subtract, multiply and divide).

first_number = float(input("Please enter the first number: "))
second_number = float(input("Please enter the second number: "))

sum = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first_number / second_number

print("The sum result is: " + str(sum))
print("The subtraction result is: " + str(subtraction))
print("The multiplication result is: " + str(multiplication))
print("The division result is: " + str(division))