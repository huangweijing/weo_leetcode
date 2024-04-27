from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        product = 1
        ans = 0
        while right < len(nums):
            product = product * nums[right]
            while left < right and left < len(nums) and product >= k:
                product //= nums[left]
                left += 1
            if product < k:
                ans += right - left + 1
            # print(left, right, ans, product)
            right += 1
        return ans

data = [
    [10,9,10,4,3,8,3,3,6,2,10,10,9,3]
    ,0
]
r = Solution().numSubarrayProductLessThanK(* data)
print(r)