from typing import List


class Solution:
    def __init__(self) -> None:
        self.start = []
        self.d = -1

    def is_okay(self, min_len: int) -> bool:
        v = self.start[0]
        for num in self.start[1:]:
            v = max(v + min_len, num)
            if v > num + self.d:
                return False
        return True
    
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        self.start = start
        self.d = d
        left, right = 0, start[-1] + d - start[0]
        mid = (left + right) >> 1
        while left < right:
            s1 = self.is_okay(mid)
            s2 = self.is_okay(mid + 1)
            if s1 and not s2:
                return mid
            elif s1 and s2:
                left = mid + 1
            elif not s1 and not s2:
                right = mid - 1
            mid = (left + right) >> 1
        return mid
    

data = [
    [2,6,13,13]
    , 5
]
r = Solution().maxPossibleScore(* data)
print(r)
