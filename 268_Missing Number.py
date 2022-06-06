class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)

sol = Solution()
r = sol.missingNumber([9,6,4,2,3,5,7,0,1])
print(r)