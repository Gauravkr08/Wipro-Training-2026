class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print()

student1 = Student("Mohan", 56)
student2 = Student("pranay", 51)
student1.display_details()
student2.display_details()