from typing import List
from sortedcontainers import SortedList
import math




class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        cost_mat = [[math.inf] * 26 for _ in range(26)]
        for i, ch in enumerate(original):
            cost_mat[ord(ch) - ord("a")][ord(changed[i]) - ord("a")] = (
                min(cost_mat[ord(ch) - ord("a")][ord(changed[i]) - ord("a")], cost[i]))
        for i in range(26):
            cost_mat[i][i] = 0
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    # print(i, j, k)
                    d1 = cost_mat[j][i]
                    d2 = cost_mat[i][k]
                    d3 = cost_mat[j][k]
                    if d1 + d2 < d3:
                        cost_mat[j][k] = d1 + d2
        # print(cost_mat)
        ans = 0
        for i, ch in enumerate(source):
            val = cost_mat[ord(ch) - ord("a")][ord(target[i]) - ord("a")]
            if val == math.inf:
                return -1
            ans += val
        return ans


data = [
    "abcd"
    , "acbe"
    , ["a", "b", "c", "c", "e", "d"]
    , ["b", "c", "b", "e", "b", "e"]
    , [2, 5, 5, 1, 2, 20]
]
r = Solution().minimumCost(* data)
print(r)

