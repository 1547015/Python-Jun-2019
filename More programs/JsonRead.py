import json
 
people_string = [
	{
		"name":"suresh",
		"phone":"99000",
		"emails":["suresh.d@gmail.com","abcd@gmail.com"]
	},
	{
		"name":"uj",
		"phone":"9963",
		"emails":["uj.d@gmail.com","abcde@gmail.com"]
	}
]
rows = []
for each in people_string:
	# print(each)
	for email in each["emails"]:
		print(email)
		rows.append([each["name"], each['phone'], email])

print(rows)

