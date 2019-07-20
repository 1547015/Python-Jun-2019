import json
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

def createTable(column_names, table_name):#api_to_sql123
	mycursor.execute("DROP TABLE if exists "+table_name)

	mycursor.execute("CREATE TABLE "+ table_name+ "("+column_names[0]+" datetime,"+column_names[1]+" decimal(50,3), "+column_names[2]+" decimal(50,3),"+column_names[3]+" decimal(50,3)," +column_names[4]+"  decimal(50,3), "+column_names[5]+" decimal(50,3),"+column_names[6].replace(" ","_")+" decimal(50,3))")
	return True

def loadData(actual_data, table_name):
	print("Loading data into "+ table_name+"...")
	for row in actual_data:
		# print("printing row", eachrow)
		try:
			statement = "insert into "+table_name+" values('"+row[0]+"',"+str(row[1])+","+str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6])+");"
			mycursor.execute(statement)
		except Exception as e:
			print("Error in parsing", row, e, table_name)

	print("Loading finished")


request = requests.get("https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_key=wCR45yAnoiMm11NqfWt4")
#status_code, text
#Status codes: 
#    200: success
#    400+: Authorization error-401 /page not found - 404
#    500+: Server side Error - 502, Gateway timeout - 504
if(request.status_code==200):
	request_text = request.text
	data = json.loads(request_text)
	# print((request.__dir__(), request.status_code))
	# print(data['dataset'].keys())
	col_names = data['dataset']['column_names']
	actual_data = data['dataset']['data']
	print(col_names, actual_data)
	createTable(col_names, "api_to_sql")
	loadData(actual_data, "api_to_sql")
	mydb.commit()	

	#data_serialize = json.dump(data, open('test.json', "w"), indent = 4)
else:
	print("error in calling API, statu code:", request.status_code)