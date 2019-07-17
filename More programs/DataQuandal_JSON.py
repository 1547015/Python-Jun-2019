import json
import requests

request = requests.get("https://www.quandl.com/api/v3/datasets/CHRIS/MGEX_IH1.json?api_key=wCR45yAnoiMm11NqfWt4")
request_text = request.text

data = json.loads(request_text)
print(type(data)

#data_serialize = json.dump(data, open('test.json', "w"), indent = 4)

