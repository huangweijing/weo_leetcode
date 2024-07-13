from typing import List


class Solution:
    def __init__(self):
        self.bloomDay = []
        self.m = 0
        self.k = 0

    def is_day_okay(self, day: int) -> bool:
        okay_day_cnt = 0
        bouquet_cnt = 0
        for d in self.bloomDay:
            if d <= day:
                okay_day_cnt += 1
            else:
                okay_day_cnt = 0
            if okay_day_cnt == self.k:
                bouquet_cnt += 1
                okay_day_cnt = 0
            if bouquet_cnt >= self.m:
                return True
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        self.bloomDay, self.m, self.k = bloomDay, m, k
        bloom_day_list = sorted(set(bloomDay))
        # bloom_day_list.append(10 ** 9)
        # print(bloom_day_list)
        if self.is_day_okay(bloom_day_list[0]):
            return bloom_day_list[0]
        l, r = 1, len(bloom_day_list) - 1
        mid = (l + r) >> 1
        while l <= r:
            mid_res = self.is_day_okay(bloom_day_list[mid])
            mid1_res = self.is_day_okay(bloom_day_list[mid - 1])
            if mid_res and not mid1_res:
                return bloom_day_list[mid]
            elif mid_res and mid1_res:
                r = mid - 1
            elif not mid_res and not mid1_res:
                l = mid + 1
            mid = (l + r) >> 1
            # print(l, r, mid)
        return -1

data = [
    [45, 84, 46]
    , 3
    , 1
]
res = Solution().minDays(* data)
print(res)