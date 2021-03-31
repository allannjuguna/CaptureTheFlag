import sys

path=(sys.argv[0])


level=(''.join(path.split('.')[0])[-1:])
host='bandit.labs.overthewire.org'
port='2220'
username='bandit'+level
password='boJ9jbbUNNfktd78OOpsqOltutMc3MY1'


command=f'ssh {username}@{host} -p {port}\n{password}'
print(command)






#We are given a file named -
#We cant read the file using cat or strings
#So we read the file using the command cat<-
#CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9


#string="The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game."
