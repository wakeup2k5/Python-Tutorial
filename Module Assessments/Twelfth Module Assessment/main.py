# Write the Fibonacci function you wrote in the last submodule, but this time with recursion.

def fibonacci_sequence(max_value, num1=0, num2=1, sequence=None):
    if sequence is None:
        sequence = [num1]
    
    if num2 > max_value:
        return sequence
    else:
        sequence.append(num2)
        return fibonacci_sequence(max_value, num2, num1 + num2, sequence)
    
max_value = 100
print(fibonacci_sequence(max_value))