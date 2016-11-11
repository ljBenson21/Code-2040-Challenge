import requests
import json
# I made a JSON string variable so that I could pass in my token and my url to github
json_string = '{"token" : "32003a47cded737d82e38ec1fc226905", "github" : "https://github.com/ljBenson21/Code-2040-Challenge.git"}'
#
sendThing = json.loads(json_string) # I loaded the JSON string variable into a variable called sendthing... couldnt think of something creative 
headers = {'content-type' : 'application/json'} # so that I could read what I posted to the web address
# posted to the website and got confirmation that I was successfully registered
r = requests.post('http://challenge.code2040.org/api/register', json = sendThing, headers = headers) 
print (r.content)

