# morning_raj_batch
# python to be integrated with mysql
# pip install mysql-connector-python
import mysql.connector
from dotenv import load_dotenv
import os

# db = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="Walden0042$$",
#   database="morning_raj_batch"
# )

load_dotenv()

db = mysql.connector.connect(
  host=os.getenv("host"),
  user=os.getenv("user"),
  password=os.getenv("password"),
  database=os.getenv("database"),
  port=os.getenv("port"),
  ssl_ca=os.getenv("ssl_ca"),
)

if db.is_connected():
  print("Connected to MySQL database")

cursor = db.cursor()

def createTable(name):
  query = f"create table if not exists {name}(id int primary key, name varchar(255), age int)"
  cursor.execute(query)

createTable("student")
print("Table created successfully")

def insertData(id,name,age):
  query = f"insert into student(id,name,age) values({id},'{name}',{age})"
  cursor.execute(query)
  db.commit()
  print("Data inserted successfully")

# insertData(1,"Arpit",23)
# insertData(2,"Darshan",24)
# print("Data Inserted Successfully")

def showData():
  query = "select * from student"
  cursor.execute(query)
  list = cursor.fetchall()
  return list

print(showData())

# update data
# delete data
