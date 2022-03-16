def number_students():
    return int(input("Enter the number of students: "))

def student_info(student_num):
    students = []
    for i in range(student_num):
        print(f"Please enter student {i+1} infor:")
        id = input("- ID: ")
        name = input("- Name: ")
        DoB = input("- DoB: ")
        students.append({"id": id, "name": name, "DoB": DoB})
    print(f"Finished entering {i+1} students")
    return students

def number_courses():
    return int(input("Enter the number of courses: "))  

def course_info(course_num):
    courses = []
    for i in range(course_num):
        print(f"Please enter course {i+1} infor:")
        id = input("- ID: ")
        name = input("- Name: ")
        courses.append({"id": id, "name": name})
    print(f"Finished entering {i+1} courses")   
    return courses

def select_course():
    return input("Select course id: ")

def input_student_mark_for_course(id, students):
    course_marks = []    
    i  = 1
    for student in students:
        print(f"Please enter student {i} mark: ")
        print(f"-ID: {student['id']}, Name: {student['name']}, DoB: {student['DoB']}")
        mark = int(input("Mark: "))
        course_marks.append({"c_id": id,"s_id": student['id'], "name": student['name'], "DoB": student['DoB'], "Mark": mark})
        i += 1
    return course_marks

def list_courses(courses):
    print(f"Listing {len(courses)} courses:")
    for course in courses:
        print(f"-ID: {course['id']}, Name: {course['name']}")

def list_students(students):
    print(f"Listing {len(students)} students:")
    for student in students:
        print(f"-ID: {student['id']}, Name: {student['name']}, DoB: {student['DoB']}")

def show_marks_for_course(id, course_marks):
    print(f"Listing course ID {id} marks:")
    for mark in course_marks:
        if(id == mark['c_id']):
            print(f"- Student ID: {mark['s_id']}, Name: {mark['name']}, DoB: {mark['DoB']}, Mark: {mark['Mark']}")

student_num = number_students()
students = student_info(student_num)
list_students(students)

course_num = number_courses()
courses = course_info(course_num)
list_courses(courses)

Selected_course_ID = select_course()
course_marks = input_student_mark_for_course(Selected_course_ID, students)
show_marks_for_course(Selected_course_ID,course_marks)