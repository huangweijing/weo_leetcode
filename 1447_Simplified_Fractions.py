from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        ans = []
        for i in range(2, n + 1):
            for j in range(1, i):
                if math.gcd(i, j) != 1:
                    continue
                ans.append(f"{j}/{i}")
        return ans
