import binascii
strings=""" 
3338382d7573657220
3133392d7573657220
3334342d7573657220
3133322d7573657220
3538342d7573657220
3434302d7573657220
3434302d7573657220
"""

strings=strings.split('\n')
strings=strings[1:-1]
for string in strings:
	fullstring=string.strip()
	partial=string[1:6]
	print(partial +' => '+(binascii.unhexlify(fullstring)).decode())
