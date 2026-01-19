from models.person import Person
from utils.descriptors import MarksDescriptor
from utils.decorators import logger

class Student(Person):

    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks
        self.courses = []

    def __del__(self):
        print(f"Student object {self.name} destroyed")

    def get_details(self):
        print("Student Details:")
        print("----------------")
        print(f"Name      : {self.name}")
        print("Role      : Student")
        print(f"Department: {self.department}")

    @logger
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)