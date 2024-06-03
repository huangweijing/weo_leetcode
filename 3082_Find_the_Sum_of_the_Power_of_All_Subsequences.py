from typing import List
from collections import defaultdict, Counter


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        dp = defaultdict(lambda: Counter())
        for i, num in enumerate(nums):
            new_dp = defaultdict(lambda: Counter())
            for sum_val, len_cnt in dp.items():
                # print(f"sum_val={sum_val}, len_cnt={len_cnt}")
                for length, cnt in len_cnt.items():
                    # print(f"length={length}, cnt={cnt}")
                    new_dp[sum_val][length] += cnt
                if sum_val + num > k:
                    continue
                else:
                    for length, cnt in len_cnt.items():
                        new_dp[sum_val + num][length + 1] += cnt
            new_dp[num][1] += 1
            dp = new_dp
            # print(dp)
        ans = 0
        mod = 10 ** 9 + 7
        for length, cnt in dp[k].items():
            ans += pow(2, len(nums) - length, mod) * (cnt % mod) % mod
            ans %= mod
        return ans


