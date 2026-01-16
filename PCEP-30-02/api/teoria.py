# Tarea: define la lógica: esperar, reintentar N veces, y si falla, error controlado (en vez de reventar todo).
import requests
import time 

cont = 0 

url='https://jsonplaceholder.typicode.com/comments'
max_retries= 3 
attempt = 0 

headers = {'Content-type': 'application/json', 'Accept':'application/json'}

def get_with_retry(url, headers, max_retries:int=3, timeout: int=10):

    while max_retries > attempt:
        try:
            r = requests.get(url=url, headers=headers, timeout=timeout )
            
            if r.status_code == 200:
                data = r.json()
                print(f'OK Recibidos {len(data)} items')
                break 
            
            # rate limit 
            if r.status_code == 429:
                retry_after = r.headers.get('Retry-After')
                
                # Si el server no manda Retry-After, usa un fallback 
                wait_seconds = int(retry_after) if (retry_after and retry_after.isdigit()) else 10 
                
                attempt +=1 
                if attempt > max_retries:
                    raise RuntimeError(f"429 persiste tras {max_retries} reintentos")
                
                time.sleep(wait_seconds)
                continue
            
            # otros errores 
            r.raise_for_status()
        except requests.exceptions.Timeout:
            attempt+= 1 
            if attempt > max_retries:
                raise RuntimeError(f"Timeout tras {max_retries} reintentos")
            continue
        
        # Errores de red, DNS, SSL, etc 
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f'Fallo request {e}, {type(e)}')
    
    raise RuntimeError("No se puedo completar la request")

resp = get_with_retry()