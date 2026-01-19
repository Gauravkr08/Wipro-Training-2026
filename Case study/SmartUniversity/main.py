from models.student import Student
from models.faculty import Faculty
from models.course import Course
from utils.generators import student_generator
from utils.file_handler import save_students_json, generate_csv_report
from utils.display import title, section, success, error


students = []
faculty_list = []
courses = []

while True:
    title("SMART UNIVERSITY MANAGEMENT SYSTEM")

    print("""
    1️⃣  Add Student
    2️⃣  Add Faculty
    3️⃣  Add Course
    4️⃣  Calculate Student Performance
    5️⃣  Compare Two Students
    6️⃣  Generate Reports
    7️⃣  Show Students
    8️⃣  Exit
    """)

    choice = input("👉 Enter your choice: ")

    try:
        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            sem = int(input("Semester: "))
            marks = list(map(int, input("Marks (5): ").split()))

            students.append(Student(sid, name, dept, sem, marks))
            section("STUDENT CREATED SUCCESSFULLY")
            print(f"ID        : {sid}")
            print(f"Name      : {name}")
            print(f"Department: {dept}")
            print(f"Semester  : {sem}")
            success("Student added to system")


        elif choice == "2":
            fid = input("Faculty ID: ")
            name = input("Name: ")
            dept = input("Department: ")
            salary = int(input("Salary: "))

            faculty_list.append(Faculty(fid, name, dept, salary))
            section("FACULTY CREATED SUCCESSFULLY")
            print(f"ID        : {fid}")
            print(f"Name      : {name}")
            print(f"Department: {dept}")
            success("Faculty added to system")


        elif choice == "3":
            code = input("Course Code: ")
            name = input("Course Name: ")
            credits = int(input("Credits: "))

            courses.append(Course(code, name, credits, faculty_list[0]))
            section("COURSE ADDED SUCCESSFULLY")
            print(f"Course Code : {code}")
            print(f"Course Name : {name}")
            print(f"Credits     : {credits}")
            print(f"Faculty     : {faculty_list[0].name}")
            success("Course assigned successfully")




        elif choice == "4":
            section("STUDENT PERFORMANCE REPORT (ALL STUDENTS)")
            if not students:
                error("No students found. Please add students first.")
            else:
                for idx, student in enumerate(students, start=1):
                    print(f"\n📘 Student {idx}")
                    print("-" * 30)
                    avg, grade = student.calculate_performance()
                    print(f"Student ID   : {student.id}")
                    print(f"Student Name : {student.name}")
                    print(f"Department   : {student.department}")
                    print(f"Semester     : {student.semester}")
                    print("Marks        :", ", ".join(map(str, student.marks)))
                    print(f"Average      : {avg:.2f}")
                    print(f"Grade        : {grade}")


        elif choice == "5":
            section("STUDENT PERFORMANCE COMPARISON")
            s1 = students[0]
            s2 = students[1]
            avg1, _ = s1.calculate_performance()
            avg2, _ = s2.calculate_performance()
            print(f"Student 1 : {s1.name}")
            print(f"Average  : {avg1:.2f}\n")
            print(f"Student 2 : {s2.name}")
            print(f"Average  : {avg2:.2f}\n")
            if s1 > s2:
                print(f"Result   : {s1.name} performed better")
            else:
                print(f"Result   : {s2.name} performed better")



        elif choice == "6":
            section("GENERATING REPORTS")
            generate_csv_report(students)
            save_students_json(students)
            success("All reports generated successfully")


        elif choice == "7":
            for record in student_generator(students):
                section("STUDENT RECORDS")
                for record in student_generator(students):
                    print("📘", record)


        elif choice == "8":
            title("THANK YOU")
            print("🙏 Thank you for using Smart University Management System")
            break

    except Exception as e:
        print(str(e))