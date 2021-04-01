#! /usr/bin/python3
import requests
import lxml.html as parser


#Link 1 https://ringzer0ctf.com/challenges/142

#Challenge Link http://challenges.ringzer0team.com:10142

session=requests.Session()
#Website details
host='http://challenges.ringzer0team.com:10142'



url=host


response=session.get(url)
content=response.text
status=response.status_code
headers=response.headers
cookies=response.cookies

# Getting the source code link and the contents of the source code
sourcecode=host+'/captcha3.txt'
# print(session.get(sourcecode,headers=custom_headers).text)




#Sending the payload 
sessionvalue=""
phpsession=f'PHPSESSID={sessionvalue}'
custom_headers={"Cookie":phpsession+';wp_woocommerce_session_7a281fb6a05a19671ea88de2bb4f0399=b7459c0d9ca386ea9966b870a3d7fd87||1612969616||1612966016||7f36141938dda67003b05de0019c15a7'}
payload={"captcha":sessionvalue}
new_response=(session.post('http://challenges.ringzer0team.com:10142/captcha3.php',headers=custom_headers,data=payload))
new_content=new_response.text
print(new_content)