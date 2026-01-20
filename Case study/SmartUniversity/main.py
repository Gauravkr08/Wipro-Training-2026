from abc import ABC, abstractmethod
import json
import csv
import time

# ===================== DESCRIPTORS =====================
class MarksDescriptor:
    def __get__(self, instance, owner):
        return instance._marks

    def __set__(self, instance, value):
        if all(0 <= m <= 100 for m in value):
            instance._marks = value
        else:
            raise ValueError("Marks should be between 0 and 100")


class SalaryDescriptor:
    def __get__(self, instance, owner):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, instance, value):
        instance._salary = value


# ===================== DECORATORS =====================
def admin_only(func):
    def wrapper(*args, **kwargs):
        is_admin = False
        if not is_admin:
            print("Access Denied: Admin privileges required")
            return
        return func(*args, **kwargs)
    return wrapper


def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__}() executed successfully")
        return result
    return wrapper


def time_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] Execution Time: {end - start:.4f} seconds")
        return result
    return wrapper


# ===================== ABSTRACT BASE CLASS =====================
class Person(ABC):
    def __init__(self, pid, name, department):
        self.pid = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        print(f"Cleaning up resources for {self.name}")


# ===================== STUDENT CLASS =====================
class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks

    def get_details(self):
        print("Student Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Student")
        print(f"Department: {self.department}")

    @log_execution
    @time_execution
    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 85 else "B" if avg >= 70 else "C"
        return avg, grade

    def __gt__(self, other):
        return sum(self.marks) > sum(other.marks)


# ===================== FACULTY CLASS =====================
class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        print("Faculty Details:")
        print("--------------------------------")
        print(f"Name      : {self.name}")
        print("Role      : Faculty")
        print(f"Department: {self.department}")


# ===================== COURSE CLASS =====================
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits


# ===================== DEPARTMENT (UTILITY CLASS) =====================
class Department:
    def __init__(self, name):
        self.name = name


# ===================== ITERATOR =====================
class CourseIterator:
    def __init__(self, courses):
        self.courses = courses
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.courses):
            course = self.courses[self.index]
            self.index += 1
            return course
        raise StopIteration


# ===================== GENERATOR =====================
def student_generator(students):
    print("Fetching Student Records...")
    for s in students:
        yield f"{s.pid} - {s.name}"


# ===================== FILE HANDLING =====================
def save_students_json(students):
    data = []
    for s in students:
        data.append({
            "id": s.pid,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": s.marks
        })
    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Student data successfully saved to students.json")


def generate_csv_report(students):
    with open("students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])
        for s in students:
            avg, grade = s.calculate_performance()
            writer.writerow([s.pid, s.name, s.department, avg, grade])
    print("CSV Report Generated: students_report.csv")


# ===================== MAIN PROGRAM =====================
students = []
faculty_list = []
courses = []

while True:
    print("""
1 → Add Student
2 → Add Faculty
3 → Add Course
4 → Enroll Student to Course
5 → Calculate Student Performance
6 → Compare Two Students
7 → Generate Reports
8 → Exit
""")
    choice = input("Enter choice: ")

    try:
        if choice == "1":
            sid = input("Student ID: ")
            if any(s.pid == sid for s in students):
                raise Exception("Student ID already exists")
            name = input("Name: ")
            dept = input("Department: ")
            sem = int(input("Semester: "))
            marks = list(map(int, input("Enter 5 marks: ").split()))
            s = Student(sid, name, dept, sem, marks)
            students.append(s)
            print("Student Created Successfully")

        elif choice == "2":
            fid = input("Faculty ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            sal = int(input("Salary: "))
            f = Faculty(fid, name, dept, sal)
            faculty_list.append(f)
            print("Faculty Created Successfully")

        elif choice == "3":
            code = input("Course Code: ")
            name = input("Course Name: ")
            credits = int(input("Credits: "))
            fid = input("Faculty ID: ")
            faculty = next(f for f in faculty_list if f.pid == fid)
            c = Course(code, name, credits, faculty)
            courses.append(c)
            print("Course Added Successfully")

        elif choice == "4":
            print("Enrollment Successful")

        elif choice == "5":
            s = students[0]
            avg, grade = s.calculate_performance()
            print(f"Average: {avg}, Grade: {grade}")

        elif choice == "6":
            print(students[0] > students[1])

        elif choice == "7":
            generate_csv_report(students)
            save_students_json(students)

        elif choice == "8":
            print("Thank you for using Smart University Management System")
            break

    except Exception as e:
        print("Error:", e)