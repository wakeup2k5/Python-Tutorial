# Build a program that helps students track their grades. Students can input the grades they achieve for each subject, 
# and the program will read their grades from a file and calculate their average grade. 
# The program should handle exceptions (e.g., invalid input, file errors) and store the grades in a file for future reference.

def add_new_grade(grades_data):
    new_course = input("Enter the course name: ")
    new_grade = input("Enter the numeric grade (0 - 100): ")
    if new_course != "" and new_grade != "" and type(new_grade) == int:
        grades_data.write(new_course + "\n")
        grades_data.write(new_grade + "\n")
    else:
        print("Course must be provided and grade must be an integer.  Please try again.")


def view_previous_grades(grades_data):
    grades_data.seek(0)
    previous_entries = grades_data.readlines()
    for idx in range(len(previous_entries)):
        if idx % 2 == 0:
            print("Course: " + previous_entries[idx].rstrip() )
        else:
            print("-> Grade: " + previous_entries[idx].rstrip() )

def calculate_average_grade(grades_data):
    grades_data.seek(0)
    previous_entries = grades_data.readlines()
    number_of_grades = len(previous_entries) / 2
    sum_of_grades = 0
    for idx in range(len(previous_entries)):
        if idx % 2 != 0:
            sum_of_grades += int(previous_entries[idx].rstrip())
    print("Overall Grades Average: " + str(sum_of_grades / number_of_grades))

def main(): 
    menu_options = {"1" : "Add a new grade", "2": "View Previous Grades", "3": "Calculate Average Grade", }

    grades_data = open("grades_data.txt", "a+")

    print("Grades Tracker")
    print("MENU")
    print("---")
    for key in menu_options:
        print(key,":", menu_options[key])
    print("---")
    selection = input("Please choose a menu number from above: ")

    try:
        if menu_options[selection] == 'Add a new grade':
            add_new_grade(grades_data)
        elif menu_options[selection] == 'View Previous Grades':
            view_previous_grades(grades_data)
        elif menu_options[selection] == 'Calculate Average Grade':
            calculate_average_grade(grades_data)

    except Exception as argument:
        print("ERROR: " + str(argument))
    finally:
        grades_data.close()

main()