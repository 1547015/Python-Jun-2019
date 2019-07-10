def square_cube(num):
	return num*num,num*num*num
x = [1,2,13,24,45,90]
for i in x:
	a,b = square_cube(i)
	print("even numbers are",a,b)