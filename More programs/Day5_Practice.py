# ------------------------------number of characters and words in a string--------

with open("C:/Users/suresh Reddy/Desktop/Python-Learning/Jun2019 batch/Test files/Splitdata.txt",'r') as f1:
	data =  f1.read()
	print("Original string is:"+data)
	char = 0
	word = 1
	for i in data:
		char = char+1
		if (i == ' '):
			word = word+1
	print("Number of words in the string:")
	print(word)
	print("Number of characters in the string:")
	print(char)		
	res =len(data.split())
 	print("Total words in the string are:"+str(res))
# # ----------------------------------------------------------------------------------------------
# f1 = open("C:\\Users\\suresh Reddy\\Desktop\\Python-Learning\\Jun2019 batch\\Test files\\demo.txt",'r')
# f2 = open("C:/Users/suresh Reddy/Desktop/Python-Learning/Jun2019 batch/Test files/evenchar.txt",'w')
# # data = f1.readlines()
# # print(f1.read())
# # print(data)
# for i in f1.readlines():
#     print(i)
#     if len(i) % 2 != 0:
#         f2.write(i+'\n')
#     else:
#         pass
# f2.close()
# --------------------------------------------------------------------------------------------------
f1 = open("C:\\Users\\suresh Reddy\\Desktop\\Python-Learning\\Jun2019 batch\\Test files\\demo.txt",'r')
count = 0
# data = f1.readlines()
for i in f1.readlines():
    if "surya" in i:
    	count = count+1
print(count)    	
f1.close()


