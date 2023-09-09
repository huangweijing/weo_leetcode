class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        ans = 0
        count1 = 0
        while total - count1 * cost1 >= 0:
            ans += (total - count1 * cost1) // cost2 + 1
            count1 += 1
        return ans
