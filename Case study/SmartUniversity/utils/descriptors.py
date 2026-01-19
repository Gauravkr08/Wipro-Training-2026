class MarksDescriptor:

    def __get__(self, instance, owner):
        return instance._marks

    def __set__(self, instance, value):
        if not all(0 <= m <= 100 for m in value):
            raise ValueError("Error: Marks should be between 0 and 100")
        instance._marks = value


class SalaryDescriptor:

    def __get__(self, instance, owner):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, instance, value):
        instance._salary = value