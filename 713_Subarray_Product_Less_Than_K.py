from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        product = nums[0]
        ans = 0
        while right < len(nums):
            while right + 1 < len(nums) and product * nums[right + 1] < k:
                right += 1
                product *= nums[right]
            print(left, right, product, ans)

            if right + 1 < len(nums):
                right += 1
                product *= nums[right]

            # cnt = right - 1 - left + 1
            # ans += cnt * (cnt + 1) // 2
            # product *= nums[right]
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            print(left, right, product)
        return ans

data = [
    [10,5,2,6]
    ,100
]
r = Solution().numSubarrayProductLessThanK(* data)
print(r)