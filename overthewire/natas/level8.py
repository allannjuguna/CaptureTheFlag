#! /usr/bin/python
import binascii
import base64
import requests
session=requests.Session()

#Functions
def cleanheaders(headers):
	for item in headers:
		value=headers.get(item,'Not Found')
		print(f'{item} : {value}')


#Basic Authentication
basic_username,basic_password='natas8:DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'.split(':')


#Website Details
host=f'http://{basic_username}.natas.labs.overthewire.org'
path='/'

#Custom Headers
custom_headers=''


#Payload
payload={'secret':'oubWYf2kBq','submit':'Submit+Query'}
url=host+path

string='3d3d516343746d4d6d6c315669563362'
reversedstring=(binascii.unhexlify(string).decode())
unreversedstring=reversedstring[::-1]
base64_decode=base64.b64decode(unreversedstring)
secret=(base64_decode.decode())




response=requests.post(url,data=payload,auth=(basic_username,basic_password))
content=response.text
status=response.status_code
headers=response.headers







flag=content.split('\n')[14]
print(flag)


#WRITEUP
#This time we have the same form but with a different secret .We also have the source code 


# <?

# $encodedSecret = "3d3d516343746d4d6d6c315669563362";

# function encodeSecret($secret) {
#     return bin2hex(strrev(base64_encode($secret)));
# }

# if(array_key_exists("submit", $_POST)) {
#     if(encodeSecret($_POST['secret']) == $encodedSecret) {
#     print "Access granted. The password for natas9 is <censored>";
#     } else {
#     print "Wrong secret";
#     }
# }
# ?>


#All we have to do is work in reverse
#As we can see ,the secret is first converted to base64 the strreversed and the converted form bin2hex
#So the first thing we do in reverse is to convert from hex2bin then reverseit then base64_decodeit
#Converting from hex2bin gives ==QcCtmMml1ViV3b
#Reversing ==QcCtmMml1ViV3b we get b3ViV1lmMmtCcQ==
# Finally we base64 decode b3ViV1lmMmtCcQ== to give us oubWYf2kBq which is the secret

#Posting the secret we get the flag natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl