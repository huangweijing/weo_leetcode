from typing import List


class Solution:
    def __init__(self):
        self.nums = []

    def get_pairs_if_threshold_is(self, diff_threshold: int):
        ans = 0
        i = 1
        while i < len(self.nums):
            if self.nums[i] - self.nums[i - 1] <= diff_threshold:
                ans += 1
                i += 1
            i += 1
        return ans


    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        self.nums = nums
        # print(nums)
        left, right = 0, nums[-1] - nums[0]
        # print(self.get_pairs_if_threshold_is(-1))
        mid = left + right >> 1

        while left <= right:
            pairs_cnt1 = self.get_pairs_if_threshold_is(mid - 1)
            pairs_cnt2 = self.get_pairs_if_threshold_is(mid)
            # print(f"left={left}, mid={mid}, right={right}, pairs_cnt1={pairs_cnt1}, pairs_cnt2={pairs_cnt2}")
            # if pairs_cnt1 == p == pairs_cnt2:
            #     return mid - 1
            if pairs_cnt1 < p <= pairs_cnt2:
                return mid
            elif p <= pairs_cnt1:
                right = mid - 1
            elif pairs_cnt2 < p:
                left = mid + 1
            mid = left + right >> 1
        return 0

data = [
    [0,5,3,4]
    , 0
]
r = Solution().minimizeMax(* data)
print(r)
