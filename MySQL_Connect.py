import mysql.connector
import csv
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "test"
)
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE if exists csv_to_sql")

mycursor.execute("CREATE TABLE csv_to_sql ( name VARCHAR(10))")
