import json

people_string = '''
{
	
	"people":[
	{
		"name"="suresh"
		"phone"="99000"
		"emails"=["suresh.d@gmail.com","abcd@gmail.com"]
	},
	{
		"name"="uj"
		"phone"="9963"
		"emails"=["uj.d@gmail.com","abcde@gmail.com"]
	}

	]
}
'''
data = json.loads(people_string)
print(data)

