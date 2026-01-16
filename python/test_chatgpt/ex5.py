# Implementa pair_sum(nums, target) 
# que devuelva una tupla con índices (i, j) tal que nums[i] + nums[j] == target, o None si no existe.
# Debe ser O(n).
# Ej: nums=[2,7,11,15], target=9 → (0,1)

def pair_sum(nums, target):
    seen = {}
    
    for i, n in enumerate(nums):
        needed = target - n
        if needed in seen:
            return(seen[needed], i)
        seen[n] = i
        
    return None
    
nums = [2,7,11,15]

print(pair_sum(nums, 26))