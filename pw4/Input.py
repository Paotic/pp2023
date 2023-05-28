from domains import Course
from domains import Students
from domains import Mark
from domains import Credit

student = []
course = []
mark = []
credit = []

def type():
    c = int(input("Number of course: "))
    for j in range (c):
        crs = Course.Course()
        course.append(Course.Course.__str__(crs))
        cr = Credit.Credit()
        credit.append(Credit.Credit.__str__(cr))
        print("\t")

    s = int(input("Number of student: "))
    for i in range (s):
        std = Students.Students()
        student.append(Students.Students.__str__(std))
        print("\t")
        for crs in course:
            m = float(input(f" {crs} Mark: "))
            Mark.Mark()
            mark.append(Mark.Mark.__str__(m)) 
     
