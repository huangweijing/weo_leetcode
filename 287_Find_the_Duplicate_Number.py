class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        num_sum = sum(nums)
        cnt = len(nums)
        return num_sum - int((cnt - 1) * cnt / 2)

r = Solution().findDuplicate([1,3,4,3,2])
print(r)
