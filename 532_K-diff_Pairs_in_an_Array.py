from typing import List
import bisect


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        pair_set = set[int]()
        # print(nums)
        for i, num in enumerate(nums):
            if num in pair_set:
                continue
            idx = bisect.bisect_right(nums, num + k, lo=i + 1)
            idx -= 1
            # print(num + k, nums, i, idx)
            if i < idx < len(nums) and nums[idx] == num + k:
                ans += 1
                # print(num + k, nums, idx - 1, i)
                pair_set.add(num)
        return ans

data = [
    [3,1,4,1,5]
    , 2
]
r = Solution().findPairs(*data)
print(r)
