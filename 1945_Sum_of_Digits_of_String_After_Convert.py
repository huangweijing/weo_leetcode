class Solution:
    def getLucky(self, s: str, k: int) -> int:
        val = 0
        for ch in s:
            str_val = str(ord(ch) - ord('a') + 1)
            val += sum([int(v) for v in str_val])
        for _ in range(1, k):
            str_val = str(val)
            val = sum([int(v) for v in str_val])
        return val
    
r = Solution().getLucky("iiii", 1)
print(r)