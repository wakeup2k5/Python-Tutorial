# Write a function to calculate factorials using recursion.

def calculate_factorial(value):
    if value > 1:
        return value * calculate_factorial(value - 1)
    else:
        return 1

print(calculate_factorial(10))