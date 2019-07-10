def iseven(num):
	if(num %2 == 0):
		return True
	else:
		return False
x = [1,2,13,24,45,90]
for i in x:
	a = iseven(i)
	if(a):
		print(i ,"is even")
	else:
		print(i ,"is odd")