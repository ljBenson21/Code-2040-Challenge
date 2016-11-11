import requests 
import json
import datetime
# this one took a bit longer
def code2040stepfive():
	json_string = '{"token" : "32003a47cded737d82e38ec1fc226905"}' 
	parsed_json = json.loads(json_string)
	headers = {'content-type': 'application/json'}
	r = requests.post('http://challenge.code2040.org/api/dating', json = parsed_json, headers = headers)
	print(r.text)
	parsed_json = json.loads(r.text)
	date = parsed_json["datestamp"] #first parse; I found that I could split up the individual items in the original ISO 8601
	year = date[:4]
	month = date[5:7]
	day = date[8:10]
	hours = date[11:13]
	minutes = date[14:16]
	sec = date[17:19]
	# after splitting them I put them all together into given time; also putting them into integers instead of strings
	givenTime = datetime.datetime(int(year), int(month) , int(day), int(hours), int(minutes), int(sec))
	print(givenTime)
	sec2Add= parsed_json["interval"] # made a seconds to add variable holding the interval
	newTime = givenTime + datetime.timedelta(seconds = sec2Add) #now that I have the data and interval separate, I add the interval
	print (newTime.isoformat()) 
	NewDateStamp = newTime.isoformat() + "Z"# turn newTime back into a string object using isoformat() that I found on the interweb with Z added
	
	json_string = {"token" : "32003a47cded737d82e38ec1fc226905", "datestamp" : NewDateStamp}
	print(json_string)
	r = requests.post('http://challenge.code2040.org/api/dating/validate', data = json.dumps(json_string), headers = headers)
	print(r.text)
# numerous print() statements are to make sure that I am getting the correct response after each step
	
code2040stepfive()
