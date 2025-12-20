import requests
from requests import Session

# Exercicio 1 
s = Session()
url = "https://jsonplaceholder.typicode.com/posts/1"
response = s.request(method='GET', url=url, verify=True)
data = response.json()

print(f"Status: {response.status_code}")
print(f"JSON completo: {data}")
print(f"Titulo: {data.get('title', '')}")

# Exercicio 2 
# print(response['title'])
# print(type(response)) # 
# print(response)
# print(response.status_code) # 200 si todo esta ok 
# print(response.headers) # headers de la respuesta 
# print(response.text) # cuerpo en bruto (string)