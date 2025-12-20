import requests
from requests import Session

# Exercicio 2
s = Session()
url = "https://jsonplaceholder.typicode.com/comments"
params = {'postId': 1}
response = s.request(method='GET', url=url, verify=True, params=params)
comments = response.json()


print(f"Numero de comentarios: {len(comments)}")
print(f"Email del primer comentario: {comments[0].get('email')}")