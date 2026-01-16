from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        print(self.name,"Salary is 25000")


m=Manager("Mohan")
m.salary()