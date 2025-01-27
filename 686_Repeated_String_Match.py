import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a.find(b) != -1:
            return 1
        str_a = a * (len(b) // len(a))
        if str_a == b:
            return len(b) // len(a)
        mod = 10 ** 9 + 7
        high = pow(27, len(b) - 1, mod)
        str_a = a * math.ceil(len(b) / len(a))
        hash_a, hash_b = 0, 0
        for i, ch in enumerate(b):
            dig = ord(ch) - ord('a') + 1
            hash_b = (hash_b * 27 + dig) % mod
        for i, ch in enumerate(str_a[: len(b)]):
            dig = ord(ch) - ord('a') + 1
            hash_a = (hash_a * 27 + dig) % mod
        
        end_idx = -1
        for i, ch in enumerate(str_a[len(b): ], start=len(b)):
            end_idx = i
            dig1 = ord(str_a[i - len(b)]) - ord('a') + 1
            dig2 = ord(ch) - ord('a') + 1
            hash_a = (hash_a - dig1 * high + mod) % mod
            hash_a = (hash_a * 27 + dig2) % mod
            if hash_a == hash_b:
                return math.ceil(len(b) / len(a))
        str_a += a
        for i, ch in enumerate(str_a[end_idx + 1: ], start=end_idx + 1):
            dig1 = ord(str_a[i - len(b)]) - ord('a') + 1
            dig2 = ord(ch) - ord('a') + 1
            hash_a = (hash_a - dig1 * high + mod) % mod
            hash_a = (hash_a * 27 + dig2) % mod
            if hash_a == hash_b:
                return math.ceil(len(b) / len(a)) + 1

        return -1

data = [
    "abc"
    , "cabcabca"
]
r = Solution().repeatedStringMatch(*data)
print(r)