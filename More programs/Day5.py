file1 = open("C:/Users/suresh Reddy/Desktop/Python-Learning/Jun2019 batch/Test files/demo.txt",'r')
file1.read()
file2 = open("C:/Users/suresh Reddy/Desktop/Python-Learning/Jun2019 batch/Test files/bglr.txt",'w')
for i in file1:
	file2.write(i+'\n')
file1.close()
file2.close()	

# with open("C:/Users/suresh Reddy/Desktop/Python-Learning/Jun2019 batch/Test files/demo.txt",'r') as f1:
# 	data =  f1.readline()
# 	print(data)
# 	for line in data:
# 		print(line.split())
