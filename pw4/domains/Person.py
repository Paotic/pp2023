class Person:
    def __init__(self):
        self.name = str(input("Student name: "))
        self.id = int(input("Student ID: "))
        self.dob = str(input("Student DoB: "))
    def __str__(self):
        return f"{self.name} {self.id} {self.dob}" 