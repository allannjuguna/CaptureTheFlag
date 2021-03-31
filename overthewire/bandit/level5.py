import sys

path=(sys.argv[0])


level=(''.join(path.split('.')[0])[-1:])
host='bandit.labs.overthewire.org'
port='2220'
username='bandit'+level
password='koReBOKuIDDepwhWk7jZC0RTdopnAYKh'


command=f'ssh {username}@{host} -p {port}\n{password}'
print(command)






#We get folder name inhere
#Changing to the dir to the folder we find a hidden file
#We find files with the format -file00
#We just read all the files using


# cat<-file00 ; cat<-file01 ; cat<-file02 ; cat<-file03 ; cat<-file04 ; cat<-file05 ; cat<-file06 ; cat<-file07 ; cat<-file08 ; cat<-file09 ; 
#The flag is in file 7
# koReBOKuIDDepwhWk7jZC0RTdopnAYKh

#string="The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game."



# grep -Eo "[a-zA-Z]{32}

# find -type f -exec grep -Eo "[a-zA-Z]{32} {} +
 # find . -type f -exec grep -Eo "[a-zA-Z]{32} {} +

