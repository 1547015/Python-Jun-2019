import mysql.connector
import csv
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "test"
)

mycursor = mydb.cursor()
mycursor.execute("DROP TABLE if exists csv_to_sql123")

mycursor.execute("CREATE TABLE csv_to_sql123 (bdate datetime,open VARCHAR(255), high VARCHAR(255),low VARCHAR(255), last VARCHAR(255),volume VARCHAR(255), open_Interst VARCHAR(255))")

with open('CSV_Testdata.csv') as csvdata:
	data = csv.reader(csvdata, delimiter = ',')
	line_count = 0
	for row in data:
		#print(row)
		if line_count != 0:

			mycursor.execute("insert into csv_to_sql123(bdate,open,high,low,last,volume,open_Interst) values ('"+row[0]+"','"+row[1]+"','"+row[2]+"','"+row[3]+"','"+row[4]+"','"+row[5]+"','"+row[6]+"');")
		line_count +=1
	mydb.commit()					