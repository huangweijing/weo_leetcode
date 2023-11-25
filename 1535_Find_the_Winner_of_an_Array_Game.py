from typing import List
from collections import deque


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        gt_cnt = [0] * len(arr)
        larger_than_prev = [False] * len(arr)
        stk = []
        for i, num in enumerate(reversed(arr)):
            smaller_cnt = 0
            while len(stk) > 0 and num > stk[-1][0]:
                v, c = stk.pop()
                smaller_cnt += 1 + c
            stk.append([num, smaller_cnt])
            gt_cnt[-1 - i] = smaller_cnt

        min_num = arr[0]
        for i, num in enumerate(arr[1:], start=1):
            if num > min_num:
                min_num = num
                larger_than_prev[i] = True
            else:
                larger_than_prev[i] = False
        for i in range(len(arr)):
            if i == 0:
                if gt_cnt[i] >= k:
                    return arr[0]
            elif larger_than_prev[i]:
                if gt_cnt[i] + 1 >= k or i + gt_cnt[i] == len(arr) - 1:
                    return arr[i]


data = [
    [1,9,8,2,3,7,6,4,5]
    , 7
    ]
r = Solution().getWinner(*data)
print(r)





