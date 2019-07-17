import json
import datetime as dt
import requests
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

mycursor.execute("CREATE TABLE csv_to_sql (bdate datetime,open VARCHAR(255), high VARCHAR(255),low VARCHAR(255), last VARCHAR(255),volume VARCHAR(255), open_Interst VARCHAR(255))")

request = requests.get("https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_key=wCR45yAnoiMm11NqfWt4")
request_text = request.text

data = json.loads(request_text)
print(data["dataset"]["data"])
for row in data["dataset"]["data"]:
	print(row)
	print("------------")
	# row[0] = dt.datetime(row[0])
	mycursor.execute("insert into csv_to_sql(bdate,open,high,low,last,volume,open_Interst) values ('"+row[0]+"','"+row[1]+"','"+row[2]+"','"+row[3]+"','"+row[4]+"','"+row[5]+"','"+row[6]+"');")
# 
	# mycursor.execute("insert into csv_to_sql(bdate) values ("+row[0]+");")
		
mydb.commit()

#data_serialize = json.dump(data, open('test.json', "w"), indent = 4)