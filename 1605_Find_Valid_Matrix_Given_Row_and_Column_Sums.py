from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = [[0] * len(colSum) for _ in range(len(rowSum))]
        for i in range(len(rowSum)):
            for j in range(len(colSum)):
                val = min(rowSum[i], colSum[j])
                rowSum[i] -= val
                colSum[j] -= val
                ans[i][j] = val
                # print(ans)
        return ans


data = [
    [3, 8]
    , [4, 7]
]
r = Solution().restoreMatrix(* data)
print(r)
