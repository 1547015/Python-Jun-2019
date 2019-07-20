import re

m = ['asd3b', 'asdas', 'asdf123', '12345','a1245']
# Match a string to a numberic sequence of exactly five
def matchNumbers(m):
	for input in m:
		m = re.match('\d{5}\Z',input)
		if m:
		    print("True")
		else:
		    print("False")
# matchNumbers(m)
emails = ['a#@wns.coom', 'gm@gmail.com@1233@@@', 'asdsd_123#123']
def matchEmails(emails):
	for input in emails:
		m = re.match('[^@]+@[^@]+\.[^@]+',input)

		if m:
		    print("True")
		else:
		    print("False")
# matchEmails(emails)

input = ["Contact me by test @example.com or at the office.", "there is no email here"]

def searchEmail(input):

	for each in input:
		m = re.search('[^@]+@[^@]+\.[^@]+',each)

		if m:
		    print("String found.")
		else:
		    print("Nothing found.")
searchEmail(input)