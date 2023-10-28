from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1, 9):
            val = 0
            for j in range(i, 10):
                val = val * 10 + j
                if val > high:
                    break
                if low <= val <= high:
                    ans.append(val)
        return sorted(ans)

r = Solution().sequentialDigits(1000,13000)
print(r)

