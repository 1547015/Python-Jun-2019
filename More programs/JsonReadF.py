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
# dehgjhg = [1,2,3]

# data = json.loads(people_string)
# print(people_string)
def my_function(x):
	p = []
	for eachppl in x:
		b = x[eachppl]
		for c in b:
			email = (c['emails'])
			for d in email:
				p.append(d)
	return p
				# print(d)
				# print("----")
print(my_function(people_string))				




# x = {'a':'b'}




