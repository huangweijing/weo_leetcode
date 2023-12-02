from typing import List
import math


class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        bean_sum = sum(beans)
        prefix_sum = 0
        ans = math.inf
        for i, bean in enumerate(beans):
            ans = min(ans, bean_sum - (len(beans) - i) * bean)
            prefix_sum += bean
        return ans
