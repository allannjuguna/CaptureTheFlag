#! /usr/bin/python3
import requests
import lxml.html as parser
import binascii


#Website details
host='https://ringzer0ctf.com/16bfff59f7e8343a2643bdc2ee76b2dc/'
url=host
custom_headers={"Cookie" : "PHPSESSID=0j7vimrdobha0uo1s9hev5vh01"}


session=requests.Session()
response=session.get(url,headers=custom_headers)
content=response.text
status=response.status_code
headers=response.headers
flag=content
print(flag)
