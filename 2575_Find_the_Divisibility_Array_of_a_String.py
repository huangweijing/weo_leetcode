from typing import List


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        mod = 0
        ans = []
        for ch in word:
            mod = (mod * 10 + int(ch)) % m
            ans.append(1 if mod == 0 else 0)
        return ans


data = [
    "998244353"
    , 3
]
r = Solution().divisibilityArray(*data)
print(r)