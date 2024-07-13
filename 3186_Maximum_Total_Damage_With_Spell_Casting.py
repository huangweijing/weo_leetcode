from typing import List


class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        power.sort()
        # [[power, damage], ..]
        dp = [0, 0, 0]
        last_power = -10
        for p in power:
            new_dp = [0, 0, 0]
            if last_power == p:
                new_dp = [dp[0] + p, dp[1], dp[2]]
            elif last_power < p - 2:
                val = max(dp) + p
                new_dp = [val, max(dp), max(dp)]
            elif last_power == p - 2:
                val = max(dp[1:]) + p
                new_dp = [val, max(dp), max(dp)]
            elif last_power == p - 1:
                val = dp[2] + p
                new_dp = [val, dp[0], max(dp[1], dp[2])]
            dp = new_dp
            last_power = p
            # print(p, dp)
        return max(dp)


data = [2,1,4,3,1,1,1,5]
print(sorted(data))
r = Solution().maximumTotalDamage(data)
print(r)
