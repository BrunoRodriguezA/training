# 1) is_even(n) sin usar %
def is_even(n: int) -> bool:
    return (n & 1) == 0  # bit menos significativo


# 2) normalize_spaces(s)
def normalize_spaces(s: str) -> str:
    return " ".join(s.split())


# 3) top_k_frequent(nums, k)
def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    # Ordenar por frecuencia desc
    return [num for num, _count in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]]


# 4) sum_by_user(sales)
def sum_by_user(sales: list[dict]) -> dict[str, int]:
    totals = {}
    for item in sales:
        user = item["user"]
        amount = item["amount"]
        totals[user] = totals.get(user, 0) + amount
    return totals


# 5) pair_sum(nums, target) en O(n)
def pair_sum(nums: list[int], target: int):
    seen = {}  # valor -> índice
    for i, n in enumerate(nums):
        needed = target - n
        if needed in seen:
            return (seen[needed], i)
        seen[n] = i
    return None


# 6) has_duplicates(items)
def has_duplicates(items: list) -> bool:
    return len(items) != len(set(items))


# 7) safe_int(s, default=None)
def safe_int(s, default=None):
    try:
        return int(s)
    except (ValueError, TypeError):
        return default


# 8) Debug only_evens(nums)
# Bug: la condición "if n % 2" es True para impares; está añadiendo impares.
def only_evens(nums: list[int]) -> list[int]:
    evens = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
    return evens


# 9) merge_intervals(intervals)
def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []

    intervals_sorted = sorted(intervals, key=lambda x: x[0])
    merged = [intervals_sorted[0]]

    for start, end in intervals_sorted[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:  # solapan o tocan
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged


# 10) is_anagram(a, b) ignorando espacios y mayúsculas
def is_anagram(a: str, b: str) -> bool:
    def clean(s: str) -> str:
        return "".join(ch.lower() for ch in s if ch != " ")

    a2 = clean(a)
    b2 = clean(b)

    if len(a2) != len(b2):
        return False

    count = {}
    for ch in a2:
        count[ch] = count.get(ch, 0) + 1

    for ch in b2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]

    return len(count) == 0