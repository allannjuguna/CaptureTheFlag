#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')



#Website Details
host='http://natas1.natas.labs.overthewire.org'
path=''

#Basic Authentication
basic_username='natas1'
basic_password='gtVrDuiDfck831PqWsLEZy5gyDz1clto'

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

flag=content.split('\n')[16]
print(flag)


#WRITEUP
#The flag was in the source of the index.html page but this time right clicking is blocked