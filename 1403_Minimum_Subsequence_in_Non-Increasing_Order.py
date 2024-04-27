from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        sum_nums = sum(nums)
        nums.sort(reverse=True)
        acc_num = 0
        ans = []
        for num in nums:
            if acc_num <= sum_nums:
                ans.append(num)
            else:
                break
            acc_num += num
            sum_nums -= num
        return ans

data = [4,3,10,9,8]
r = Solution().minSubsequence(data)
print(r)

