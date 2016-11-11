import requests
import json

def code2040step3():
	json_string = '{"token" : "32003a47cded737d82e38ec1fc226905"}'
	parsed_json = json.loads(json_string)
	headers = {'content-type': 'application/json'}
	r = requests.post('http://challenge.code2040.org/api/haystack', json = parsed_json, headers = headers)
	print (r.text)
	parsed_json = json.loads(r.text)
	
	list = parsed_json["haystack"]
	i = 0
	while i < len(list):
		if parsed_json["needle"] == list[i]:
			break
		i += 1
		
	json_string = '{"token" : "32003a47cded737d82e38ec1fc226905", "needle" : "'+str(i)+'"}'
	parsed_json = json.loads(json_string)
	r = requests.post('http://challenge.code2040.org/api/haystack/validate', json = parsed_json, headers = headers)
	print(r.text)
	'''
def code2040stepthree(token):
	tok = {"token": token}
	dictResponse = requests.post("http://challenge.code2040.org/api/haystack", data=json.dumps(tok))
	index = needleHelper(json.loads(dictResponse.text))
	result = {"token": token, "needle": index}
	print(result)
	'''
	
code2040step3()