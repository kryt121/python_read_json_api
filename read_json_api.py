import requests

url="http://verdaduras.com.pl/api_testy/index.php/user/list?limit=20"
resp = requests.get(url=url)
data = resp.json() 

print(data)
