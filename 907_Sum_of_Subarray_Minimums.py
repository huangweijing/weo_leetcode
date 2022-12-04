from typing import List
from collections import deque

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        i, q = len(arr) - 1, deque()
        sum_min_arr = [0] * len(arr)
        while i >= 0:
            while len(q) > 0 and arr[i] < q[-1][0]:
                q.pop()
            if len(q) > 0:
                sum_min_arr[i] = arr[i] * (q[-1][1] - i) + sum_min_arr[q[-1][1]]
            else:
                sum_min_arr[i] = arr[i] * (len(arr) - i)
            q.append([arr[i], i])
            sum_min_arr[i] %= (10 ** 9 + 7)
            i -= 1
        return sum(sum_min_arr) % (10 ** 9 + 7)

r = Solution().sumSubarrayMins([11,81,94,43,3])
print(r)

