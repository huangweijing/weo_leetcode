class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_dist = math.inf
        ans = -1
        for num in nums:
            if min_dist > abs(num):
                ans = num
                min_dist = abs(num)
            elif min_dist == abs(num):
                ans = max(num, ans)
        return ans

