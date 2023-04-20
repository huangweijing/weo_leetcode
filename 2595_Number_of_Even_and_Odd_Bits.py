from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ns = bin(n)[2:]
        ans = [0, 0]
        for i, ch in enumerate(reversed(ns)):
            if ch == "1":
                if i & 1 == 0:
                    ans[0] += 1
                else:
                    ans[1] += 1
        return ans

r = Solution().evenOddBit(2)
print(r)