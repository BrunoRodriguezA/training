# Implementa top_k_frequent(nums, k) que devuelva una lista
# con los k números más frecuentes (en cualquier orden).
# Ej: nums=[1,1,1,2,2,3], k=2 → [1,2]

def top_k(nums,k):
    freq = {}
    # itera solo 1 vez (O(n))  en vez de (O(n2)) usando un count 
    for num in nums:
        freq[num] = freq.get(num,0) + 1 
        
    # lista de tuplas (n, count)
    items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(items)
    # recorre la tupla y solo se queda con el n, hasta la posicion k 
    
    return [num for num, _count in items[:k]]
        
nums = [1,1,1,2,2,3]
k = 1

print(top_k(nums, k))
