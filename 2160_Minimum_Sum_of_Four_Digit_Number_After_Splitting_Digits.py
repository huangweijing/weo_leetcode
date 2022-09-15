class Solution:
    def minimumSum(self, num: int) -> int:
        nums = []
        while num > 0:
            nums.append(num % 10)
            num = int(num / 10)
        nums.sort()
        return (nums[0] + nums[1]) * 10 + nums[2] + nums[3]

r = Solution().minimumSum(3241)
print(r)
