import requests
session=requests.Session()
filtered="# "
url="http://52.28.216.196/skiddy/"
links="index.php flag.php flag1.jpg robots.txt.php"

for link in links.split(' '):
	link=url+link
	response=session.get(link)
	content=response.text
	# if failed.lower() not in content.lower():
	if 'flag1.jpg' in link:
		filename='flag1.jpg'
		file=open(filename,'wb')
		file.write(response.content)
		file.close()
		print(f'[+] Written {link} to {filename} ')
	else:
		print(f'{link}\n')