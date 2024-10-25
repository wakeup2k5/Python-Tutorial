# Write the Fibonacci function you wrote in the last submodule, but this time with recursion.

def fibonacci_sequence(length, sequence=None):
    if sequence is None:
        if length > 1:
            sequence = [0, 1] 
        else: 
            sequence = [0] 

    if len(sequence) >= length:
        return sequence
    else:
        sequence.append(sequence[-1] + sequence[-2])
        return fibonacci_sequence(length, sequence)
    

quantityRequested = int(input("Please enter the number of fibonacci numbers to display: "))
print("Fibonacci sequence of length", quantityRequested, ":", fibonacci_sequence(quantityRequested))