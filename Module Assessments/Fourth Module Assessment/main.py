# Calculate the area and circumference of a circle given the inputs from the user. 
# You are given the required radius input from the user. 
# Print out the area and circumference of the circle.

pi = 3.141592653589793

radius = float(input("Please enter the radius of the circle (cm): "))

circumference = 2 * pi * radius
area = pi * (radius ** 2)

print(f"The circumference is: {circumference} cm")
print(f"The area is: {area} square cm")

