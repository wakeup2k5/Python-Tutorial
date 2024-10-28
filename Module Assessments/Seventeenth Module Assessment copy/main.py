# Create a simple student database system that stores information about students, such as their names, ages, and grades.
# Use classes to represent students and include methods for displaying student information and calculating average grades.

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def displayGrades(self):
        for key in self.grades:
            print(key + ": " + str(self.grades[key]))

    def displayStudentInformation(self):
        print("Name: " + self.name)
        print("Age: " + str(self.age))
        self.displayGrades()

student1Grades = {"Math":90, "Physics": 85, "English": 75}
student1 = Student("James Collins", 21, student1Grades)

student2Grades = {"Math":95, "Physics": 80, "English": 75}
student2 = Student("Jane Doe", 20, student2Grades)

students = [student1]
students.append(student2)

addAnotherStudent = input("Would you like to add another student? (Y/N): ")
if(addAnotherStudent == "Y"):
    anotherStudentName = input("Enter the Students Name: ")
    anotherStudentAge = input("Enter the Students Age: ")
    anotherStudentMathGrade = input("Enter the Students Math Grade: ")
    anotherStudentPhysicsGrade = input("Enter the Students Physics Grade: ")
    anotherStudentEnglishGrade = input("Enter the Students English Grade: ")
    anotherStudent = Student(anotherStudentName, anotherStudentAge, {"Math":anotherStudentMathGrade, "Physics": anotherStudentPhysicsGrade, "English": anotherStudentEnglishGrade})
    students.append(anotherStudent)

for student in students:
    print("---------------")
    student.displayStudentInformation()


    

