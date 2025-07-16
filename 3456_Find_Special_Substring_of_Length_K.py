class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        last = ""
        sub_len = 0
        for _, ch in enumerate(s):
            if ch == last:
                sub_len += 1
            else:
                if sub_len == k:
                    return True
                sub_len = 1
            last = ch
        if sub_len == k:
            return True
        return False
    

data = [
    "11112333"
    , 3
]
r = Solution().hasSpecialSubstring(*data)
print(r)