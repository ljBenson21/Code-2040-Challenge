import requests
import json


def code2040StepTwo():
	json_string = '{"token" : "32003a47cded737d82e38ec1fc226905"}'
	stringThing = json.loads(json_string)
	headers = {'content-type': 'application/json'}
	r = requests.post('http://challenge.code2040.org/api/reverse', json = stringThing, headers = headers)
	print(r.content)
	str = r.text # created a string of the text sent to me
	rev = "" # I created a string called reverse that is set to nothing
	print(str)
	for c in str: # after each loop the character c is added into the reverse string
		rev = c + rev
	
	json_string = '{"token" : "32003a47cded737d82e38ec1fc226905" , "string" : "'+rev+'"}' 
	stringThing = json.loads(json_string)
	r = requests.post('http://challenge.code2040.org/api/reverse/validate', json = stringThing, headers = headers)
	print(r.content)

code2040StepTwo()
