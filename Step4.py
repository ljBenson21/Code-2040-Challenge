import requests
import json


def code2040step4():
	json_string = '{"token" : "32003a47cded737d82e38ec1fc226905"}'
	stringThing = json.loads(json_string)
	headers = {'content-type': 'application/json'}
	r = requests.post('http://challenge.code2040.org/api/prefix', json = stringThing, headers = headers)
	print (r.text)
	parsed_json = json.loads(r.text)
	list = parsed_json["array"] # parse one
	substr = parsed_json["prefix"] # parse two
	noPrfArray = [] # created a new array to hold the strings that did not have the prefixes in them
	for string in list:
		if string.find(substr) == -1: # if the string did not have the prefix then add it to the no prefix array
			noPrfArray.append(string)

	
	print (str(noPrfArray))
	json_string = {"token" : "32003a47cded737d82e38ec1fc226905", "array" : noPrfArray}
	# this is where I learned the difference between dumping my JSON string and passing my JSON stringThing
	r = requests.post('http://challenge.code2040.org/api/prefix/validate', data = json.dumps(json_string), headers = headers)
	print(r.text)
	
	
	
	
code2040step4()

