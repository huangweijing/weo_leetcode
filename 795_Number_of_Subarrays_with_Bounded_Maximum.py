from typing import List
from collections import deque


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ng_arr, ok_arr = deque(), deque()
        for i, num in enumerate(nums):
            if left <= num <= right:
                ok_arr.append(i)
            if num > right:
                ng_arr.append(i)
        ng_arr.append(len(nums))
        ans = 0
        # print(ok_arr,  ng_arr)
        for i, num in enumerate(nums):
            if len(ok_arr) > 0 and ok_arr[0] < i:
                ok_arr.popleft()
            if len(ng_arr) > 0 and ng_arr[0] < i:
                ng_arr.popleft()
            if len(ok_arr) > 0 and ng_arr[0] > ok_arr[0]:
                # print(i, num, ng_arr, ok_arr, ng_arr[0] - ok_arr[0])
                ans += ng_arr[0] - ok_arr[0]
        return ans
    


data = [
    [5]
    , 2
    , 8
]
r = Solution().numSubarrayBoundedMax(* data)
print(r)

        