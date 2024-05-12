from typing import List
from collections import deque
import bisect


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left_arr, right_arr = deque(), deque()
        for num in arr:
            if len(left_arr) == 0:
                left_arr.append(num)
            elif left_arr[-1] <= num:
                left_arr.append(num)
            else:
                break
        if len(left_arr) == len(arr):
            return 0
        for num in reversed(arr):
            if len(right_arr) == 0:
                right_arr.append(num)
            elif right_arr[0] >= num:
                right_arr.appendleft(num)
            else:
                break
        ans = len(arr)
        for i, num in enumerate(left_arr):
            idx = bisect.bisect_left(right_arr, num)
            seq_len = i + 1 + len(right_arr) - idx
            ans = min(len(arr) - seq_len, ans)
            # print(num , seq_len)
        ans = min(len(arr) - len(right_arr), len(arr) - len(left_arr), ans)
        return ans


data = [16,10,0,3,22,1,14,7,1,12,15]
r = Solution().findLengthOfShortestSubarray(data)
print(r)