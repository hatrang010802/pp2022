def number_students():
    return int(input("Enter the number of students: "))

def student_info():
    st_id = input("Enter student's id: ")
    st_name = input("Enter student's name: ")
    DoB = input("Enter student's date of birth: ")
    return st_id, st_name, DoB

def number_courses():
    return int(input("Enter the number of courses: "))  

def course_info():
    c_id = input("Enter id of the course: ")
    c_name = input("Enter the name of the course: ")
    return c_id, c_name

#print the list of students
st_num = number_students()
list_student = []     
for i in range(st_num):
    st_id,st_name,DoB = student_info()
    list_student.append((st_id,st_name,DoB)) 
print("\n")
print("The list of students: ") 
for s in list_student:
    print(f"Student ID: {s[0]}    Name: {s[1]}    DoB: {s[2]}") 

#print the list of courses
c_num = number_courses()            
list_course = []
for i in range(c_num):
    c_id,c_name = course_info()
    list_course.append((c_id,c_name))
print("\n")
print("The list of courses: ") 
for c in list_course:
    print(f"Course ID:{c[0]}   Name: {c[1]}")

marks = {}  
n = int(input("Enter number of marks: "))
for i in range(n):
    st_id = input ("Enter student id: ")
    c_id = input ("Enter course id: ")
    mark = int (input ("Enter marks: "))
    if c_id in marks:
        marks[c_id].append ((st_id, mark))
    else:
        marks[c_id] = [(st_id, mark)]

c_id = input ("See student marks of course id: ")
if c_id in marks:
    for x in marks[c_id]:
        print (f"Student id:{x[0]} gots mark:{x[1]}")

