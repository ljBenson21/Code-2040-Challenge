import requests
import json

def code2040step3():
	json_string = '{"token" : "32003a47cded737d82e38ec1fc226905"}'
	stringThing = json.loads(json_string)
	headers = {'content-type': 'application/json'}
	r = requests.post('http://challenge.code2040.org/api/haystack', json = stringThing, headers = headers)
	print (r.text)
	
	stringThing = json.loads(r.text)# I loaded the text received into stringthing to parse the two objects needle and haystack
	
	list = stringThing["haystack"] # first parse
	i = 0
	while i < len(list):
		if stringThing["needle"] == list[i]: # second parse; once found, the loop will break and the index will be returned
			break
		i += 1
	# "'+str(i)+'" gave me trouble because I did not know how to send the index, I did not know the correct syntax until I looked it up
	json_string = '{"token" : "32003a47cded737d82e38ec1fc226905", "needle" : "'+str(i)+'"}' 
	stringThing = json.loads(json_string)
	r = requests.post('http://challenge.code2040.org/api/haystack/validate', json = stringThing, headers = headers)
	print(r.text)

	
code2040step3()
