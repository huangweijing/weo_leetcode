from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n & 1 == 1:
            return list(range(-(n >> 1), (n >> 1) + 1))
        if n & 1 == 0:
            return [i for i in range(-(n >> 1), (n >> 1) + 1) if i != 0]

r = Solution().sumZero(4)
print(r)

