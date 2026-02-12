import mysql.connector
host="localhost"
user="root"
password="Gaurav@121"
database="feb2026"

conn=mysql.connector.connect(host=host,user=user,password=password,database=database)
cursor=conn.cursor()
print("connected to the database successfully")

query="SELECT * FROM employee"
cursor.execute(query)

result=cursor.fetchall()

for row in result:
    print(row)
