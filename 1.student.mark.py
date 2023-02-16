student = []
course = []
mark = []

def input_func():
    n = int(input("Number of course: "))
    print("Course number: ", n)
    for i in range(n):
        course.append((
            int(input("Course ID: ")),
            str(input("Course name: ")),
        ))
        print("-------")
    s = int(input("Number of student: "))
    for i in range(s):
        student.append((
            int(input("Enter student ID: ")),
            str(input("Enter student name: ")),
            str(input("Enter student DoB: ")),
    ))

        std_mark = []
        for crs in course:
            std_mark.append(float(input(f"Course {crs[1]} mark: ")))
        mark.append(std_mark)
        print("---------")    
    
def list_func():
    for idx, std in enumerate(student):
        print(f"""
              Student: {std[1]}
            
                student ID: {std[0]}
                student name: {std[1]}
                student DoB: {std[2]}
              """)
        for jdx, crs in enumerate(course):
            print(f"""
              Course ID: {crs[0]}
              Course name: {crs[1]}
              Course Mark: {mark[idx][jdx]}
              """)
        
input_func()
list_func()