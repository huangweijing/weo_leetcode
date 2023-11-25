class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        sum_nums = sum(nums)
        prefix_sum = 0
        ans = []
        for i, num in enumerate(nums):
             prefix_sum += num
             v1 = (sum_nums - prefix_sum) - num * (len(nums) - 1 - i)
             v2 = num * (i + 1) - prefix_sum
             ans.append(v1 + v2)
        return ans