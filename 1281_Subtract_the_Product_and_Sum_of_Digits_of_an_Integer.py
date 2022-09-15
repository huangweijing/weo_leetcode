from functools import reduce

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nums = list(map(int, list(str(n))))
        return reduce(lambda a, b: a * b, nums) - sum(nums)
