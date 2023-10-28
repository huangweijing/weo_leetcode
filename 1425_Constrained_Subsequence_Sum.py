import heapq
import math
from collections import deque
from typing import List


# class Item(object):
#     def __init__(self, val: int, idx: int):
#         self.val = val
#         self.idx = idx
#
#     def __lt__(self, other):
#         return self.val > other.val
#
#     def __str__(self):
#         return str(self.val) + ", " + str(self.idx)
#
# heap = []
# heapq.heappush(heap, Item(-10, 1))
# heapq.heappush(heap, Item(-18, 3))
# heapq.heappush(heap, Item(-9, 2))
# print(list(map(str, heap)))
# heapq.heappop(heap)
# print(list(map(str, heap)))



class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        q = deque()
        ans = -math.inf
        for i, num in enumerate(nums):
            if len(q) > 0:
                if q[0][0] + num > num:
                    q_new = [q[0][0] + num, i]
                else:
                    q_new = [num, i]
            else:
                q_new = [num, i]
            if len(q) > 0 and q[0][1] + k <= i:
                q.popleft()
            while len(q) > 0 and q[-1][0] <= q_new[0]:
                q.pop()
            q.append(q_new)
            ans = max(q[0][0], ans)
            # print(f"i={i} num={num}, q={q}, ans={ans}")
        return ans


data = [
    [10,10,10,10,-10,-1,-10,-1,-10,10,10,10,10]
    , 3
]
r = Solution().constrainedSubsetSum(* data)
print(r)

