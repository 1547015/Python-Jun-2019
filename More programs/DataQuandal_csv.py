
#csv_file = open('CSV_Testdata.csv')
#for row in csv_file:
#	print(row.split(','))
#there is problem with \n which is unwanted data here..better to go with csv library to avoid this issue

import csv
with open('CSV_Testdata.csv') as csvdata:
	data = csv.reader(csvdata, delimiter = ',')
	line_count = 0
	for row in data:
		if line_count == 0:
			print("this is header:%s" % (','.join(row)))
			print("this is header:%s" % (row))
			line_count +=1
		else:
			print("row number %s contains:%s"% (line_count,row))
			line_count +=1
	print("the number of rows processed:%d"% (line_count-1))		

