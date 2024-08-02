from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        cnt = 0
        ans = 0
        for cite in reversed(citations):
            cnt += 1
            if cite >= cnt:
                ans = cnt
        return ans
    
r = Solution().hIndex([0,1,3,5,6])
print(r)