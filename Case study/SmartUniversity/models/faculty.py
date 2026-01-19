from models.person import Person
from utils.descriptors import SalaryDescriptor

class Faculty(Person):

    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        print("Faculty Details:")
        print("----------------")
        print(f"Name      : {self.name}")
        print("Role      : Faculty")
        print(f"Department: {self.department}")