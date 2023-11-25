from typing import List


class Solution:
    def __init__(self):
        self.dist_arr = []
        self.sum_dist_arr = []
        self.nums = []
        self.k = 0

    def calc_dist(self, idx1: int, idx2: int) -> int:
        return self.sum_dist_arr[idx1] - self.sum_dist_arr[idx2] - \
               self.dist_arr[idx2] * (idx2 - idx1)

    def is_ans_okay(self, ans: int) -> bool:
        for i in range(ans - 1, len(self.nums)):
            if self.calc_dist(i - (ans - 1), i) <= self.k:
                return True
        return False

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        self.nums, self.k = nums, k
        self.dist_arr = [nums[-1] - n for n in nums]
        self.sum_dist_arr = []
        sum_dist = 0
        for dist in reversed(self.dist_arr):
            sum_dist += dist
            self.sum_dist_arr.append(sum_dist)
        self.sum_dist_arr = self.sum_dist_arr[::-1]
        left, right = 1, len(nums)
        mid = left + right >> 1
        while left <= right:
            check1 = self.is_ans_okay(mid)
            check2 = self.is_ans_okay(mid + 1)
            if check1 and not check2:
                return mid
            elif check1 and check2:
                left = mid + 1
            elif not check1 and not check2:
                right = mid - 1
            mid = left + right >> 1
        return mid

data = [
    [3,9,6]
    , 2
]
sol = Solution()
r = sol.maxFrequency(*data)
# print(sol.calc_dist(1, 4))
print(r)