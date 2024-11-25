from typing import List
from collections import deque


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        plants = deque(plants)
        ca, cb = capacityA, capacityB
        ans = 0
        while len(plants) > 0:
            if len(plants) == 1:
                if max(ca, cb) < plants[0]:
                    ans += 1
                plants.pop()
            else:
                if ca < plants[0]:
                    ca = capacityA
                    ans += 1
                ca -= plants.popleft()
                if cb < plants[-1]:
                    cb = capacityB
                    ans += 1
                cb -= plants.pop()
            # print(plants, ca, cb)
        return ans
            

data = [
    [1,2,4,4,5]
    , 6
    , 5
    ]
r = Solution().minimumRefill(*data)
print(r)