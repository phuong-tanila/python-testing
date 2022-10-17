import requests
import json 
res = requests.get('https://dog.ceo/api/breed/shiba/images/random')
print(res.json()['message'])