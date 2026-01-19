import json
import csv
import os


def save_students_json(students):
    os.makedirs("data", exist_ok=True)

    data = []
    for s in students:
        data.append({
            "id": s.id,
            "name": s.name,
            "department": s.department,
            "semester": s.semester,
            "marks": s.marks
        })

    with open("data/students.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Student data successfully saved to students.json")



def generate_csv_report(students):
    os.makedirs("data", exist_ok=True)

    with open("data/students_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])

        for s in students:
            avg, grade = s.calculate_performance()
            writer.writerow([s.id, s.name, s.department, round(avg, 2), grade])

    print("CSV report generated successfully")
