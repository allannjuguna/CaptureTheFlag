import sys

path=(sys.argv[0])


level=(''.join(path.split('.')[0])[-1:])
host='bandit.labs.overthewire.org'
port='2220'
username='bandit'+level
password='UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK'


command=f'ssh {username}@{host} -p {port}\n{password}'
print(command)






#We get folder name inhere
#Changing to the dir to the folder we find a hidden file
#run strings .hidden to get the pass

# pIwrPrtPN36QITSp3EQaw936yaFoFgAB

#string="The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game."
