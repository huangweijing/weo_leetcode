from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ans = 0
        left, right = 0, 0
        cnt = 1 if nums[right] % modulo == k else 0
        while right < len(nums) and cnt % modulo != k:
            right += 1
            cnt += 1 if nums[right] % modulo == k else 0

        while left < len(nums):
            right_cnt = 0
            while right < len(nums) and nums[right] % modulo != k:
                right_cnt += 1
                right += 1
            while left < right and nums[left] % modulo 

        sub_len = 0
        for num in nums:
            if num % modulo == k:
                sub_len += 1
            else:
                sub_len = 0
            if sub_len % modulo == k:
                ans += 1
        return ans


data = [
    [3,2,4]
    , 2
    , 1
]
r = Solution().countInterestingSubarrays(*data)
print(r)