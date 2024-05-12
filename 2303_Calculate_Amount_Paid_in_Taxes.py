from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        level = 0
        ans = 0
        for b in brackets:
            ans += (min(b[0], income) - level) * b[1] / 100
            level = b[0]
            if level >= income:
                break
        return ans


data = [
[[1,0],[4,25],[5,50]]
, 2
]
r = Solution().calculateTax(* data)
print(r)