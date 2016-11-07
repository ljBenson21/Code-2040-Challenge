# Code-2040-Challenge
//Step one of the Tech Assessment 
import requests
import json
json_string = '{"token" : "32003a47cded737d82e38ec1fc226905", "github" : "https://github.com/ljBenson21/Code-2040-Challenge.git"}'
parsed_json = json.loads(json_string)
headers = {'content-type' : 'application/json'}
r = requests.post('http://challenge.code2040.org/api/register', json = parsed_json, headers = headers)
print (r.content)


//Step Two
str = 'yqmczewr'
rev = ""
for c in str:
	rev = c + rev

print(rev)
