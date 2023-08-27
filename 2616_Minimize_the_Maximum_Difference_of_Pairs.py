from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        diff_list = []
        for i in range(1, len(nums)):
            diff = abs(nums[i] - nums[i - 1])
            diff_list.append(diff)
        diff_list.sort()
        print(nums)
        print(diff_list)
        if p == 0:
            return 0
        return diff_list[p - 1]


data = [
    [3,4,2,3,2,1,2]
    , 3
]
r = Solution().minimizeMax(* data)
print(r)
