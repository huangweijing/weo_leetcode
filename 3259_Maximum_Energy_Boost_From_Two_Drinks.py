from typing import List


class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        dp = [energyDrinkA[0], energyDrinkB[0], 0]
        for i in range(1, len(energyDrinkA)):
            new_dp = [0, 0, 0]
            new_dp[0] = max(dp[0] + energyDrinkA[i], dp[2] + energyDrinkA[i])
            new_dp[1] = max(dp[1] + energyDrinkB[i], dp[2] + energyDrinkB[i])
            new_dp[2] = max(dp[0], dp[1])
            dp = new_dp
        return max(dp)

