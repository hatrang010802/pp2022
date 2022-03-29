class students:
    def __init__(self,id,name,DoB):
        self.id = id
        self.name = name
        self.DoB = DoB

    def info(self,i):
        print(f"Please enter student {i+1} infor:")
        self.id = input("- Student ID: ")
        self.name = input("- Student Name: ")
        self.DoB = input("- DoB: ")

    def describe(self):
        print(f"- Student ID: {self.id}  - Student Name: {self.name}  - Birthday: {self.DoB}")

class courses:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.mark = []
    
    def info(self,i):
        print(f"Please enter course {i+1} infor:")
        self.id = input("- Course ID: ")
        self.name = input("- Course Name: ")

    def describe(self):
        print(f"- Course ID: {self.id}  - Course Name: {self.name}")
    
    def input_mark(self,num):
        for i in range(num):
            print(f"Please enter student {i} mark: ")
            mark = int(input("Mark: "))
            self.mark.append({'course_id':self.id, 'mark':mark})

    def show_mark(self):
        print(f"Listing course ID {self.id} marks:")
        for mark in self.mark:
            print(f"- ")

    # def select_course():
    #     return input("Select course id: ")

class Myclass(students,courses):
    def __init__(self):
        self.list_students = []
        self.list_courses = []

    def student_num(self):
        return int(input("Enter the number of students: "))

    def course_num(self):
        return int(input("Enter the number of courses: ")) 

    def input_students(self,num):
        for i in range(num):
            student = students()
            student.info(i)
            self.list_students.append(student)
    
    def list_student(self):
        print(f"Listing {self.student_num()} students:")
        for student in self.list_students :
            student.describe()
    
    def input_courses(self,num):
        for i in range(num):
            course = courses()
            course.info(i)
            self.list_courses.append(course)
    
    def list_course(self):
        print(f"Listing {self.course_num()} courses:")
        for course in self.list_courses :
            course.describe()

    def input_marks(self):
        pass

    def show_marks(self):
        pass



# student_num = number_students()
# students = student_info(student_num)
# list_students(students)

# course_num = number_courses()
# courses = course_info(course_num)
# list_courses(courses)

# Selected_course_ID = select_course()
# course_marks = input_student_mark_for_course(Selected_course_ID, students)
# show_marks_for_course(Selected_course_ID,course_marks)