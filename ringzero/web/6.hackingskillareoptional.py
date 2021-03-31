#! /usr/bin/python3
import requests
import lxml.html as parser

session=requests.Session()
#Website details
host='https://ringzer0ctf.com/challenges/297'
phpsession='PHPSESSID=0j7vimrdobha0uo1s9hev5vh01'
phpsession=phpsession+';flag=1; __gads=ID=e75162129edcde5f-220a81e4a2a600b5:T=1610651720:RT=1610651720:S=ALNI_MZYo4etZq3fymohq5Rho9ZelSlEBw; gadsTest=test; _ga=GA1.2.206858975.1610651719; _gid=GA1.2.519857400.1612793617'
custom_headers={"Cookie":phpsession}


url=host


response=session.get(url,headers=custom_headers)
content=response.text
status=response.status_code
headers=response.headers
cookies=response.cookies

print(cookies)
print(content)

# if 'Words mean' in content:
# 	# print(content)
# 	root=parser.fromstring(content)
# 	result=root.xpath('//div[@class="challenge-wrapper"]//text()')

# 	flag=''.join(result)
# 	print(flag.strip())
# else:
# 	pass