class Students:
    def __init__(self):
        self.name = str(input("Student name: "))
        self.id = int(input("Student ID: "))
        self.dob = str(input("Student DoB: "))   
    def __str__(self):
        return f"""
                Student ID: {self.id} 
                Student name: {self.name} 
                Student DoB: {self.dob}"""
    