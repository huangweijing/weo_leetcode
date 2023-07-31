from typing import List
import bisect


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # plus_arr = []
        nums.sort()
        print(nums)
        min_arr = []
        for num in nums:
            # plus_arr.append(num + k)
            min_arr.append(num - k)

        ans = 0
        for i, num in enumerate(nums):
            rightest_idx = bisect.bisect_right(min_arr, num + k)
            # print(rightest_idx - i)
            ans = max(rightest_idx - i, ans)
        return ans

data = [
    [4,6,1,2]
    , 2
]
r = Solution().maximumBeauty(* data)
print(r)