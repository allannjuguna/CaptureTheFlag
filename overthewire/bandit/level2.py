import sys

path=(sys.argv[0])


level=(''.join(path.split('.')[0])[-1:])
host='bandit.labs.overthewire.org'
port='2220'
username='bandit'+level
password='CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9'


command=f'ssh {username}@{host} -p {port}\n{password}'
print(command)






#We are given a file name 'spaces in this filename'
#To get the contents we run
	#strings 'spaces in this filename'
	# strings spaces\ in\ this\ filename
#UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK


#string="The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game."
