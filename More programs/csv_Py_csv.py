#csv_file = open('CSV_Testdata.csv')
#for row in csv_file:
#	print(row.split(','))
#there is problem with \n which is unwanted data here..better to go with csv library to avoid this issue

import csv
with open('Load_csv.csv', 'w' , newline='') as output:
	with open('C:/Users/suresh Reddy/Desktop/Python-Learning/Jun2019 batch/Test files/CSV_Testdata.csv') as csvdata:
		output_data = csv.writer(output,delimiter = '-')
		data = csv.reader(csvdata, delimiter = ',')
		line_count = 0
		for row in data:
			output_data.writerow(row)
			# print(row)
			# if line_count == 0:
			# 	output_data.writerow(row)
			# 	# print(row)
			# 	line_count +=1
			# else:
			# 	output_data.writerow(row)
			# 	# print(row)
			# 	line_count +=1
		print("the number of rows processed:%d"% (line_count-1))		

