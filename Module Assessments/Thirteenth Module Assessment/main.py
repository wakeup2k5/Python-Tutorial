# Write a function to calculate the average of the numbers in a list of items using the built-in sum function

def calculate_average(arr):
    retVal = sum(arr) / len(arr)
    return retVal

randomNumbers = [ 555, 8, 3, 0, 1, 7, 5, 2, 9, 4, 6 , 11, 200, 4, 2]
print(calculate_average(randomNumbers))
