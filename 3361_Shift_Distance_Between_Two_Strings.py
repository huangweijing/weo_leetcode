from typing import List


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        ans = 0
        for i, ch1 in enumerate(s):
            ch2 = t[i]
            cost_right, cost_left = 0, 0
            while ch1 != ch2:
                cost_right += nextCost[ord(ch1) - ord('a')]
                if ch1 == 'z':
                    ch1 = 'a'
                else:
                    ch1 = chr(ord(ch1) + 1)
                    
            ch1 = s[i]
            while ch1 != ch2:
                cost_left += previousCost[ord(ch1) - ord('a')]
                if ch1 == 'a':
                    ch1 = 'z'
                else:
                    ch1 = chr(ord(ch1) - 1)
            ans += min(cost_left, cost_right)
        return ans