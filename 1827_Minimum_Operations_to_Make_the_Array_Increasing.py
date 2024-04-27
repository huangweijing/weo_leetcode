class Solution:
    def minOperations(self, nums: List[int]) -> int:
        max_val = nums[0]
        ans = 0
        for num in nums[1:]:
            if num <= max_val:
                ans += max_val + 1 - num
                max_val += 1
            else:
                max_val = num
        return ans
