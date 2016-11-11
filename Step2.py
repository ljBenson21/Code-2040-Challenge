import requests
import json


def code2040StepTwo():
	json_string = '{"token" : "32003a47cded737d82e38ec1fc226905"}'
	parsed_json = json.loads(json_string)
	headers = {'content-type': 'application/json'}
	r = requests.post('http://challenge.code2040.org/api/reverse', json = parsed_json, headers = headers)
	print(r.content)
	str = r.text
	rev = ""
	print(str)
	for c in str:
		rev = c + rev
	
	json_string = '{"token" : "32003a47cded737d82e38ec1fc226905" , "string" : "'+rev+'"}' 
	parsed_json = json.loads(json_string)
	r = requests.post('http://challenge.code2040.org/api/reverse/validate', json = parsed_json, headers = headers)
	print(r.content)

code2040StepTwo()
