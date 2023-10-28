import math
from typing import List
from collections import Counter


class Solution:

    def is_valid(self, val_list: list[int], grp_cnt: int) -> bool:
        # print(val_list, grp_cnt)
        for val in val_list:
            mod = val % grp_cnt
            div = val // grp_cnt
            # print(div, mod, end=", ")
            if mod > div:
                return False
        return True

    def calc_group(self, val_list: list[int], grp_cnt: int) -> int:
        ret = 0
        for val in val_list:
            ret += math.ceil(val / (grp_cnt + 1))
        return ret


    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        # nums = [3,2,3,2,3]
        num_cnt = Counter(nums)
        val_list = list(num_cnt.values())
        # print(val_list)
        for i in reversed(range(1, min(val_list) + 1)):
            # print(i)
            if self.is_valid(val_list, i):
                return self.calc_group(val_list, i)

        # left, right = 1, 10 ** 5
        # left, right = 1, min(val_list)
        left, right = 1, min(val_list)
        mid = left + right >> 1
        while left < right:
            sub1 = self.is_valid(val_list, mid)
            sub2 = self.is_valid(val_list, mid + 1)
            print(left, right, mid, sub1, sub2, val_list)
            if sub1 and not sub2:
                break
            elif sub1 and sub2:
                left = mid + 1
            elif not sub1 and not sub2:
                right = mid - 1
            mid = left + right >> 1
        print(mid, val_list)
        ans = 0
        for val in val_list:
            # if val < mid + 1:
            #     ans += 1
            # else:
            ans += math.ceil(val / (mid + 1))
        return ans


# data = [10,10,10,10,10,3,3,1,1]
# data = [3,2,3,2,3,3,3,3,3,3,1,1,1,1,1,2]
data = [3,2,3,2,3,3,3,3,3,3,2,2,2,2,1,1,1,1,1,1,1,2]
# cnt = list(Counter(data).values())
# print(Solution().is_valid(cnt, 1))
r = Solution().minGroupsForValidAssignment(data)
print(r)
