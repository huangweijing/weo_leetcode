from typing import List
from functools import cache
from collections import Counter


class Solution:
    bit_map = {
        num: i for i, num in enumerate([2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    }

    @cache
    def key(self, num) -> int:
        ret = 0
        i = 2
        while num >= 1 and i <= num:
            while num % i == 0:
                num //= i
                if ret & (1 << Solution.bit_map[i]) > 0:
                    return -1
                else:
                    ret |= 1 << Solution.bit_map[i]
            i += 1
        return ret

    def squareFreeSubsets(self, nums: List[int]) -> int:
        dp = Counter()
        mod = 10 ** 9 + 7
        for num in nums:
            key = self.key(num)
            if key == -1:
                continue
            new_dp = dp.copy()
            # if key in dp:
            new_dp[key] = (dp[key] + 1) % mod
            # else:
            #     dp[key] = 1
            keys = list(dp.keys())
            for k in keys:
                if k & key == 0:
                    new_dp[k | key] = (new_dp[k | key] + dp[k]) % mod
            dp = new_dp
            # print(num, dp)
        return sum(dp.values()) % mod
        # return 
    

data = [3,2,3,15,18]
# data = [1,2,6,15,7,19,6,29,28,24,21,25,25,18,9,6,20,21,8,24,14,19,24,28,30,27,13,21,1,23,13,29,24,29,18,7]
data = [1, 2, 1]
# data = [3,4,4,5]
# data = [26,6,4,27,6,18]
# data = [3,2,7,8,14,19,21,28,3,15,18]

r = Solution().squareFreeSubsets(data)
print(r)