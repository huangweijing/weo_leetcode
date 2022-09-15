class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 1)
        nums[: 2] =[0, 1]
        i = 0
        result = 0
        while 2 * i + 1 <= n:
            nums[2 * i] = nums[i]
            nums[2 * i + 1] = nums[i] + nums[i + 1]
            result = max(result, nums[2 * i + 1], nums[2 * i])
            i += 1
        return result

r = Solution().getMaximumGenerated(7)
print(r)
