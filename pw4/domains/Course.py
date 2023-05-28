class Course:
    def __init__(self):
        self.__course_id = int(input("Course ID: "))
        self.__course_name = str(input("Course name: "))
    def __str__(self):
        return f"""
                Course ID: {self.__course_id} 
                Course name: {self.__course_name}"""