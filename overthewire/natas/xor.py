import base64
original='ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D'
cookie="ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw="
cipher=base64.b64decode(cookie)
cipher=((cipher.decode()))
# string=cookie
string='{"showpassword":"no","bgcolor":"#ffffff"}'
key='qw8J'

def encrypt(string,key):
	result=''
	for index in range(len(string)):
		result+=chr(ord(string[index]) ^ ord(key[index%len(key)]))
	return result


cipher=base64.b64decode('FzczAUgCJAYa').decode()
string=f'READ:path'

result=(encrypt(cipher,string))
print(result)
# print(base64.b64encode(encrypt('{"showpassword":"yes","bgcolor":"#000000"}',key).encode()).decode())


# function saveData($d) {
#     setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
# }


# 		json_encode($d)
# 	xor_encrypt()
# base64_encode()


# $mydata =  array( "showpassword"=>"no", "bgcolor"=>"#ffffff");


# 		base64_decode($_COOKIE["data"])
# 	xor_encrypt(
# 		#result is in json
# json_decode( 
#  #RESULT IS AN ARRAY
# 	Array
# (
#     [showpassword] => no
#     [bgcolor] => #ffffff
# )
