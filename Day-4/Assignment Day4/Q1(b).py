#  Create a class student that:
# 2. Has a method display_details() to print student information


class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
student1 = Student("Mohan", 56)
student1.display_details()
student2 = Student("Pranay", 61)
student2.display_details()