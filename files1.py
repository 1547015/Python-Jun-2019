a = open("C:/Users/suresh Reddy/Desktop/Python-Learning/Jun2019 batch/Test files/demo.txt",'r')
b = open("C:/Users/suresh Reddy/Desktop/Python-Learning/Jun2019 batch/Test files/demo_09072019.txt",'w')
# print(a.read())
for i in a.readlines():
	print(i)
	b.write(i)