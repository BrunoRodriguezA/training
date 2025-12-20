import requests
from requests import Session
import json 

# Exercicio 2
s = Session()
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "title": "Mi primer post desde Python",
    "body": "Este es el cuerpo del post",
    "userId": 123    
}

# application/x-www-form-urlencoded, cuando no se indica los headers 
headers = {'Content-type': 'application/json', 'Accept':'application/json'}

# response = s.request(method='POST', url=url, verify=True, data=payload)
# response = s.request(method='POST', url=url, verify=True, data=json.dumps(payload), headers=headers) # apis 
response = s.post(url, json=payload, headers=headers) # en apis 

data = response.json()
print(f"Status code: {response.status_code}")
print(f"JSON: {data}")
print(f"id: {data.get('id','')}")
