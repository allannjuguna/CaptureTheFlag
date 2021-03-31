#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username='natas2'
basic_password='ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path='/files/users.txt'


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



# print(f'HOST : {host} \n')
# cleanheaders(headers)
flag=content.split('\n')[-4]
print(flag)


#WRITEUP
#Visiting the page we find some text saying that 'There is nothing in this page'
#Checking the source we find a link 'files/pixel.png'
#Checking for other files in the files folder we find users.txt which has natas3 and the flag