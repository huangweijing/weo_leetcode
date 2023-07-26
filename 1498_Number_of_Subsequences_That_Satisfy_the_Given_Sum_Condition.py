from typing import List
import bisect


class Solution:
    MODULO = 10 ** 9 + 7

    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        for idx, num in enumerate(nums):
            wanted_num = target - num
            target_idx = bisect.bisect_right(nums, wanted_num)
            if target_idx < idx:
                break
            if target_idx >= len(nums):
                target_idx = len(nums) - 1
            target_num = nums[target_idx]
            if target_num + num > target:
                target_idx -= 1
                if target_idx < idx:
                    continue
                # target_num = nums[target_idx]
            # print(num, target_num, idx, target_idx)
            ans = (ans + (1 << (target_idx - idx + 1) - 1)) % Solution.MODULO
        return ans


data = [
    [3,3,6,8]
    # [2,3,3,4,6,7]
    , 10
]
r = Solution().numSubseq(*data)
print(r)