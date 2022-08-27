import heapq
from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        result = 0
        while len(s) > 0:
            while len(g) > 0 and g[-1] > s[-1]:
                g.pop()
            if len(g) > 0:
                result += 1
                g.pop()
                s.pop()
            else:
                break
        return result


data_g = [1,2,3]
data_s = [1,1]
r = Solution().findContentChildren(data_g, data_s)
print(r)

