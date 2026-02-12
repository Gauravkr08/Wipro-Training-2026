import pandas as pd

data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)
it_employees = df[df["Department"] == "IT"]
print("Employees from IT Department:")
print(it_employees)

avg_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary per Department:")
print(avg_salary)
df["Salary_Adjusted"] = df["Salary"] * 1.10

print("\nFinal DataFrame with Adjusted Salary:")
print(df)
