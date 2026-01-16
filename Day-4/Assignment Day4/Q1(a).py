#   create a class student that:
#   has attributes name and roll_no

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
student1 = Student("Mohan", 56)
print(student1.name)
print(student1.roll_no)  