#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')



#Website Details
host='http://natas0.natas.labs.overthewire.org'
path=''

#Basic Authentication
basic_username='natas0'
basic_password='natas0'

#Custom Headers
custom_headers=''


#Payload
payload=''
url=host+path

session=requests.Session()
response=requests.get(url,auth=(basic_username,basic_password))
content=response.text
status=response.status_code
headers=response.headers


print(content.split('\n')[15])


#WRITEUP
#The flag was in the source of the index.html page