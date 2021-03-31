#! /usr/bin/python3
import requests

session=requests.Session()

#Website details that we need
host='http://challenges.ringzer0team.com:10138'
path=''
challengename='' # For writing the output to a file
phpsession=''
custom_headers={"Cookie":f'PHPSESSID={phpsession}'}
server=''
cookie=''


#Making the headers readable
def cleanheaders(headers):
	global cookie,server
	print('HEADERS\n')
	for item in headers:
		if item.lower() == 'set-cookie':
			cookie+=headers.get(item)+','
		elif item.lower() == 'server':
			server=headers.get(item)
		else:
			pass
		print('\t'+item + ' : '+headers.get(item))


#For performing get requests
def getpage(url,custom_headers):
	print(f'\t[+] Getting : {url}\n')
	if (len(custom_headers) == 0):
		response=session.get(url)
	else:
		response=session.get(url,headers=custom_headers,allow_redirects=False)
	
	return response.text,response.headers,response.status_code

#Printing the headers and the page content in an organised manner
def show(headers,content):
	print(f'{cleanheaders(headers)}\n\n\nCONTENT\n{content}\n\n\n')




#Reading the robots.txt file
def checkrobots():
	global host
	robots_file=host+'/robots.txt'
	print(f'[*] Reading Robots.txt file at {robots_file} ...\n') 
	content,headers,status=getpage(robots_file,'')
	show(headers,content)



def checksitemap():
	global host
	sitemap_file=host+'/sitemap.xml'
	print(f'[*] Reading Sitemap.xml file at {sitemap_file} ...\n') 
	content,headers,status=getpage(sitemap_file,'')
	show(headers,content)


def checkcookies():
	print(f'[*] PLEASE CHECK COOKIES MANUALLY\n\n\n\n')




#Checking files in suspicious folders
folders='inc includes hint secret flag js css app api'.split(' ')
def checkfolders():
 pass

#Reading file source code of main files eg. index.php,index.html,index,js
def readsource(custom_headers):
	global host
	print(f'[*] Reading main file at {host} ...\n') 
	content,headers,status=getpage(host,custom_headers)
	show(headers,content)

#Reading file by filename
def readfile(filename,custom_headers):
	print(f'[*] Reading {filename} ...\n') 
	content,headers,status=getpage(filename,custom_headers)
	show(headers,content)

#Checking robots.txt file
checkrobots()

#Checking for a sitemap file
checksitemap()

#Checking for cookies
checkcookies()

#Reading page source of the main file(index files)
readsource('')

#Reading a file on the server by filename
readfile(f'{host}/form1.php','')



print(f'\nHOST : {host}\nSERVER : {server}\nCOOKIE : {cookie}\nPHPSESSION : {phpsession}')