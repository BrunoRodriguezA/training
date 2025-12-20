import json 
from requests import Session
from pathlib import Path

pathfile = Path(__file__).parent/'pikachu.json'

s = Session()

result = s.request(method='GET', url='https://pokeapi.co/api/v2/pokemon/pikachu', verify=False).json()


print(json.dumps(result, indent=4))

with open(pathfile, 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)
    
