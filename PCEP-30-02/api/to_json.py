import json 
data = {"name": "Pikachu", "level": 25}

payload = json.dumps(data)
print(type(payload))

x = json.loads(payload)
print(type(x))