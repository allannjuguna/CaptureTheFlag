import requests
session=requests.Session()

# url="http://18.192.3.151/join-team/index.php?jobs"
url="http://localhost:4050"
filename="somefile.pdf"

content="""
This is nothing
"""

test_file=open(filename,'w')
test_file.write(content)
test_file.close()

data={}
files={"cv":"somethingelse"}
response=session.post(url,files=files,data=data)

print(response.content)