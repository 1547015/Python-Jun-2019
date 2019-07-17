import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database = "test"
)
mycursor = mydb.cursor()

mycursor.execute("DROP TABLE if exists users")

mycursor.execute("CREATE TABLE users (name varchar(10),phone int,emails varchar(100))")


import json
people_string = {	"people":[
	{
		"name": "suresh",
		"phone": "99000",
		"emails": ["suresh.d@gmail.com","abcd@gmail.com"]
	},
	{
		"name": "uj",
		"phone": "9963",
		"emails": ["uj.d@gmail.com","abcde@gmail.com"]
	}

	]
}
def my_function(x):
	for eachppl in x:
		b = x[eachppl]
		for c in b:
			mycursor.execute("insert into users(name,phone) values ('"+c['name']+"',"+c['phone']+");")
	mydb.commit()
my_function(people_string)