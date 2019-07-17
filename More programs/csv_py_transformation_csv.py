
#csv_file = open('CSV_Testdata.csv')
#for row in csv_file:
#	print(row.split(','))
#there is problem with \n which is unwanted data here..better to go with csv library to avoid this issue

import csv
with open('Load_transformation_csv.csv', 'w') as output:
	with open('CSV_Testdata.csv') as csvdata:
		output_data = csv.writer(output,delimiter = ',')
		data = csv.reader(csvdata, delimiter = ',')
		line_count = 0
		for row in data:
			if line_count == 0:
				#print(type(row))
				row.append('diff')
				#print(row)
				output_data.writerow(row)
				line_count +=1
			else:
				row.append(float(row[2]) - float(row[3]))
				output_data.writerow(row)
				line_count +=1
		print("the number of rows processed:%d"% (line_count-1))		

