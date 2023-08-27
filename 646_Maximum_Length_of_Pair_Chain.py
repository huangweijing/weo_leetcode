from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: [x[1], x[0]])
        ans = []
        for pair in pairs:
            if len(ans) == 0 or ans[-1][1] < pair[0]:
                ans.append(pair)
        return len(ans)

data = [[1,2],[7,8],[4,12],[9,10]]
r = Solution().findLongestChain(data)
print(r)
