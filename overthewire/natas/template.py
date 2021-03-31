#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path=''

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



print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
cleanheaders(headers)


flag=content
print(flag)


#WRITEUP
#The flag was in the source of the index.html page but this time right clicking is blocked