import json
import requests
request = requests.get("https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_key=wCR45yAnoiMm11NqfWt4")
#status_code, text
#Status codes: 
#    200: success
#    400+: Authorization error-401 /page not found - 404
#    500+: Server side Error - 502, Gateway timeout - 504
if(request.status_code==200):
	request_text = request.text
	data = json.loads(request_text)
	# print((request.__dir__(), request.status_code))
	print(data['dataset'].keys())
	col_names = data['dataset']['column_names']
	actual_data = data['dataset']['data']
	print(col_names, actual_data)
	#data_serialize = json.dump(data, open('test.json', "w"), indent = 4)
else:
	print("error in calling API, statu code:", request.status_code)