# Calculate the - given the inputs from the user. 
# You are given the required radius input from the user. 
# Print out the area and circumference of the circle.

pi = 3.141592653589793

radius = float(input("Please enter the radius of the circle (cm): "))

circumference = 2 * pi * radius
area = pi * (radius ** 2)

ls=[2,8,6,5,2,7,9]   

    ## Type your code here 

index = -1

for ind in range(len(ls)):
    if ls[ind] % 2 != 0:
        index = ind
        break

#####################  


print(index)