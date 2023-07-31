import math
from typing import List

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        ans = -math.inf
        odd_max = -math.inf
        even_max = -math.inf
        if nums[0] & 1 == 0:
            even_max = nums[0]
        else:
            odd_max = nums[0]
        # print(f"num={nums[0]}, odd_max={odd_max}, even_max={even_max}")
        for num in nums[1:]:
            if num & 1 == 0:
                s1 = odd_max + num - x
                s2 = even_max + num
                even_max = max(s1, s2)
            else:
                s1 = odd_max + num
                s2 = even_max + num - x
                odd_max = max(s1, s2)
            # print(f"num={num}, s1={s1}, even_max={s2}")
            ans = max(odd_max, even_max)
        return ans

data = [
    [2,3,6,1,9,2]
    , 5
]
r = Solution().maxScore(*data)
print(r)