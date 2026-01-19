def student_generator(students):
    print("Fetching Student Records...")
    print("---------------------------")
    for s in students:
        yield f"{s.id} - {s.name}"