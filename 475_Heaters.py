import math
from typing import List
import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for house in houses:
            min_dis = math.inf
            idx = bisect.bisect_left(heaters, house)
            if idx == len(heaters):
                min_dis = min(min_dis, abs(house - heaters[idx - 1]))
            elif idx == 0:
                min_dis = min(min_dis, abs(house - heaters[idx]))
            else:
                min_dis = min(min_dis, abs(house - heaters[idx]), abs(house - heaters[idx - 1]))
            ans = max(ans, min_dis)
        return ans

data = [
    [1, 5]
    , [2]
]
r = Solution().findRadius(* data)
print(r)