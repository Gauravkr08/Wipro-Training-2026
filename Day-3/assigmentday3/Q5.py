class MyDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance._salary
    def __set__(self, instance, value):
        if value<0:
            raise ValueError("Value Error")
        instance._salary=value
    def __delete__(self, instance):
        raise AttributeError("Attribute Error")

class Employee:
    salary=MyDescriptor()
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
    def __str__(self):
        return f"Employee(name={self._name},Salary={self._salary})"

try:
    emp1=Employee(name="A ",salary=100000)
    emp2=Employee(name="B ",salary=50000)
    emp3=Employee(name="C ",salary=-70000)
except ValueError:
    print("Value Error")


print(emp1)
print(emp2)


try:
    emp1.salary=-10000
except ValueError:
    print("Value Error")