from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        for b in batteryPercentages:
            if b - ans > 0:
                ans += 1
        return ans


data = [0,1,2]
r = Solution().countTestedDevices(data)
print(r)
