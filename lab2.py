class Student:
    def __init__(self):
        self.id = input("Enter Student ID: ")
        self.name = input("Enter Student Name: ")
        self.dob = input("Enter Student Birthday: ")
        self.mark = []

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_mark(self):
        return self.mark

    def input_mark(self,course_id, course_mark):
        self.mark.append((course_id,course_mark))

    def __str__(self):
        return f"- Student ID: {self.id}   Student Name: {self.name}    Student DoB: {self.dob}"

class Course:
    def __init__(self):
        self.id = input("Enter Course ID: ")
        self.name = input("Enter Course Name: ")

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def __str__(self):
        return f"- Course ID: {self.id}   Course Name: {self.name}"

class MyClass:
    def __init__(self):
        self.student_num = 0
        self.course_num = 0
        self.students = []
        self.courses = []

    def get_student_num(self):
        return self.student_num

    def get_course_num(self):
        return self.course_num

    def get_students(self):
        return self.students

    def get_courses(self):
        return self.courses

    def set_student_num(self):
        self.student_num = int(input("Enter the number of students: "))
        print(f"Enter information of {self.get_student_num()} students: ")
        self.set_students()

    def set_course_num(self):
        self.course_num = int(input("Enter the number of courses: "))
        print(f"Enter information of {self.get_course_num()} courses: ")
        self.set_courses()

    def set_students(self):
        for i in range(self.get_student_num()):
            print(f"- Student Number {i+1}: ")
            self.students.append(Student())
        self.list_students()

    def set_courses(self):
        for i in range(self.get_course_num()):
            print(f"- Course Number {i+1}: ")
            self.courses.append(Course())
        self.list_courses()

    def list_students(self):
        print(f"Listing {self.get_student_num()} students: ")
        for student in self.get_students():
            print(student)
        
    def list_courses(self):
        print(f"Listing {self.get_course_num()} courses: ")
        for course in self.get_courses():
            print(course)


def main():
    aclass = MyClass()
    print("""Select one option in the following options:
        1. Enter number of students
        2. Enter number of courses
        3. Enter students information
        4. Enter courses information
        5. Enter student marks for a course
        6. List students
        7. List courses """)

    option = input("Select an option: ")

    if option == 1:
        aclass.set_student_num()

    elif option == 2:
        aclass.set_course_num()

    elif option == 3:
        aclass.set_students()

    elif option == 4:
        aclass.set_courses()

    elif option == 5:
        aclass.list_courses()
        selected_course = input("Select a course ID: ")
        for student in aclass.get_students():
            print(student)
            student.input_mark(selected_course,int(input("- Mark: ")))

    elif option == 6:
        aclass.list_students()

    elif option == 7:
        aclass.list_courses()

if __name__ == "__main__":
    main()