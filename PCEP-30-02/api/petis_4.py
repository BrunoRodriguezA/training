from requests import Session

url = 'https://jsonplaceholder.typicode.com/posts'
s = Session()
params = {'userId': 1}
result = s.get(url=url, params=params)
data = result.json()

# Haz una petición GET con params={"userId": 1} usando Session
# print(data)
print(f"Numero total de post del userId 1: {len(data)}")
for elem in data:
    title = elem.get('title','')
    if len(title) > 20:
        print(f"titulo:{title}")