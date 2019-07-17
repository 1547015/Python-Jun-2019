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

# data = json.loads(people_string)
# print(people_string)
for eachppl in people_string:
	b = people_string[eachppl]
	for c in b:
		email = (c['emails'])
		for d in email:
			print(d)
		print("----")


# x = {'a':'b'}




