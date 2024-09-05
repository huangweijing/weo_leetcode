from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        cnt = len(rolls) + n
        sum_val = mean * cnt - sum(rolls)
        ans = [1] * n
        sum_val -= n
        if sum_val < 0:
            return []
        for i in range(n):
            if sum_val >= 5:
                ans[i] = 6
                sum_val -= 5
            elif sum_val > 0:
                ans[i] = 1 + sum_val
                sum_val = 0
            else:
                break
        if sum_val > 0:
            return []
        return ans

        