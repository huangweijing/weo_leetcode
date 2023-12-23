from typing import List
from collections import Counter


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort(reverse=True)
        mod_cnt = Counter()
        ans_val = Counter()
        for num in nums:
            mod_cnt[num % space] += 1
            ans_val[num % space] = num
        max_num = 0
        ans = -1
        for key in mod_cnt.keys():
            if mod_cnt[key] > max_num:
                ans = ans_val[key]
                max_num = mod_cnt[key]
            elif mod_cnt[key] == max_num:
                ans = min(ans, ans_val[key])

        return ans
