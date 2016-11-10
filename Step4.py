import requests
import json


def code2040step4():
	json_string = '{"token" : "32003a47cded737d82e38ec1fc226905"}'
	parsed_json = json.loads(json_string)
	headers = {'content-type': 'application/json'}
	r = requests.post('http://challenge.code2040.org/api/prefix', json = parsed_json, headers = headers)
	print (r.text)
	parsed_json = json.loads(r.text)
	list = parsed_json["array"]
	substr = parsed_json["prefix"]
	noPrfArray = []
	for string in list:
		if string.find(substr) == -1:
			noPrfArray.append(string)

	
	print (str(noPrfArray))
	json_string = {"token" : "32003a47cded737d82e38ec1fc226905", "array" : noPrfArray}
	#parsed_json = json.loads(json_string)
	r = requests.post('http://challenge.code2040.org/api/prefix/validate', data = json.dumps(json_string), headers = headers)
	print(r.text)
	
	
	
	
code2040step4()

