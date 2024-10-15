# Write a program to calculate age of a person/item. 
# The program takes two inputs from the user(year person born/item created and current year) 
# and prints out the age of the person/item.

start_year = input('Please enter the start_year: ')
end_year = input('Please enter the end_year: ')

age = int(end_year) - int(start_year)

print('Age will be ' + str(age) + ' this year')
