from typing import List


class Solution:
    def __init__(self):
        self.position = []
        self.m = 0

    def my_sol(self, force: int) -> bool:
        cnt = 1
        pos = force + self.position[0]
        for p in self.position[1:]:
            if p >= pos:
                pos = p + force
                cnt += 1
            if cnt >= self.m:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        self.m, self.position = m, position
        self.position.sort()
        if self.my_sol(position[-1] - position[0]):
            return position[-1] - position[0]
        l, r = 0, position[-1] - position[0]
        mid = (l + r) >> 1
        while l < r:
            mid_force = self.my_sol(mid)
            mid1_force = self.my_sol(mid + 1)
            if mid_force and not mid1_force:
                return mid
            elif mid_force and mid1_force:
                l = mid + 1
            elif not mid_force and not mid1_force:
                r = mid
            mid = (l + r) >> 1
        return -1


data = [
    [1, 2, 3, 4, 7]
    , 3
]
res = Solution().maxDistance(*data)
print(res)