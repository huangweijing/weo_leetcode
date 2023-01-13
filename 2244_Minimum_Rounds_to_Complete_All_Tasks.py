import math
from typing import List
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        keys = list(cnt.keys())
        keys.sort()
        ans = 0
        for key in keys:
            if cnt[key] == 1:
                return -1
            else:
                ans += math.ceil(cnt[key] / 3)
        return ans

r = Solution().minimumRounds([5,5,5,5])
print(r)
