# Write a program that sorts an array ascendingly using bubble sort.

randomNumbers = [ 555, 8, 3, 0, 1, 7, 5, 2, 9, 4, 6 , 11, 200, 4, 2]

for j in range(len(randomNumbers)): # repeat for length of list
   for i in range(len(randomNumbers)): # sorts one number into the correct position
        if i < len(randomNumbers) - 1:
            if randomNumbers[i] >= randomNumbers[i+1]:
                temp = randomNumbers[i]
                randomNumbers[i] = randomNumbers[i+1]
                randomNumbers[i+1] = temp
            
print(randomNumbers)


