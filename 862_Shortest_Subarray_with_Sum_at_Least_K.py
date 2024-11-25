from typing import List
import bisect


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        presum_left_arr = [[0, -1]]
        presum_right_arr = [[0, -1]]
        presum = 0
        for i, num in enumerate(nums):
            presum += num
            while len(presum_left_arr) > 0 and presum_left_arr[-1][0] >= presum:
                presum_left_arr.pop()
            presum_left_arr.append([presum, i])
            if presum > presum_right_arr[-1][1]:
                presum_right_arr.append([presum, i])
        print(f"presum_left_arr={presum_left_arr}")
        print(f"presum_right_arr={presum_right_arr}")
        ans = 10e9
        for i, pair in enumerate(presum_right_arr):
            num = pair[0]
            idx = bisect.bisect_left(presum_right_arr, [num + k, 0])
            print(f"num={num}, x={num + k}, idx={idx}")
            if idx == len(presum_right_arr):
                continue
            ans = min(ans, presum_right_arr[idx][1] - pair[1])
        if ans == 10e9:
            ans = -1
        return ans

data = [
[45,95,97,-34,-42]
, 21
]
r = Solution().shortestSubarray(*data)
print(r)