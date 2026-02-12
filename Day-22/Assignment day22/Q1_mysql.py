import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="company_db"
)

cursor = conn.cursor()

print("\nEmployees with salary > 50000:")
cursor.execute("SELECT * FROM employees WHERE salary > 50000")
for row in cursor.fetchall():
    print(row)

insert_query = "INSERT INTO employees (name, department, salary) VALUES (%s, %s, %s)"
values = ("Harsh", "CSE", 60000)
cursor.execute(insert_query, values)
conn.commit()
print("\nNew employee inserted successfully!")

update_query = """
UPDATE employees 
SET salary = salary * 1.10 
WHERE name = %s
"""
cursor.execute(update_query, ("Harsh",))
conn.commit()
print("\nSalary updated by 10%!")

cursor.close()
conn.close()
