import csv
from shutil import copy

# print(csv.__dir__())
src = 'C:\\Users\\suresh Reddy\\Desktop\\Python-Jun-2019\\Test files\\Sourcepath'
dst = 'C:\\Users\\suresh Reddy\\Desktop\\Python-Jun-2019\\Test files\\Targetpath'
csvdata = open('C:\\Users\\suresh Reddy\\Desktop\\Python-Jun-2019\\Test files\\Testsheet.csv')
input_data = csv.reader(csvdata)
import os
filenames = os.listdir(src)

def copy_file(file_name):
	for each in filenames:
		if(file_name==each):
			copy(src+"\\"+file_name, dst)
			print(file_name)
		# print(each)


for index,each in enumerate(input_data):
	print("index::::", index)
	file_name_index = 0
	if(index==0):
		file_name_index = each.index('Filename')
	else:
		# print(each)
		if(".txt" in each[file_name_index]):
			copy_file(each[file_name_index])

# ['line1', 'line2']
# {0:"line1", 1:"line2"}