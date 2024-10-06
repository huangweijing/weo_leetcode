from typing import List
from collections import deque
import math


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seat_q = deque()
        for i, seat in enumerate(seats):
            if seat == 1:
                seat_q.append(i)
        left = -1
        # right = seat_q[0]
        ans = 0
        for i, seat in enumerate(seats):
            if seat == 1:
                left = i
            if len(seat_q) > 0 and i > seat_q[0]:
                seat_q.popleft()
            if len(seat_q) == 0:
                right = -1
            else:
                right = seat_q[0]
            if seat == 0:
                left_dist, right_dist = math.inf, math.inf
                if left >= 0:
                    left_dist = max(ans, i - left)
                if right >= 0:
                    right_dist = max(ans, right - i)
                ans = max(ans, min(left_dist, right_dist))
        return ans


data = [1,0,0,0,1,0,1]
r = Solution().maxDistToClosest(data)
print(r)


