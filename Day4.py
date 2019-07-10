# a = open("C:/Users/suresh Reddy/Desktop/Python-Learning/Jun2019 batch/demo.txt",'r')
a = open("C:/Users/suresh Reddy/Desktop/Python-Learning/Jun2019 batch/Test files/demo.txt",'r')
b = open("C:/Users/suresh Reddy/Desktop/Python-Learning/Jun2019 batch/Test files/evenchar.txt",'w')
# data1 = a.read()
# print(data1)
for i in a.readlines():
	i = i.replace('\n','')
	# print([i,"-------------",len(i)%2])
	print(i)
	if(len(i)%2 ==0):
		# print(i,"hello")
		b.writelines(i+'\n')

	else:
		print("odd")	
b.close()