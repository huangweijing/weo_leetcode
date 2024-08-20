from typing import List
from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        ans = 0
        for key, val in cnt.items():
            key_cnt = (val // (key + 1)) * (key + 1)
            if val % (key + 1) > 0:
                key_cnt += key + 1
            ans += key_cnt
        return ans

r = Solution().numRabbits([10, 10, 10])
print(r)

        