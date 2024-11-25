from typing import List


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        dp1 = [[0] * len(mat[0]) for _ in mat]
        ans = 0
        for i, row in enumerate(mat):
            dp = []
            sum_val = 0
            for j, _ in enumerate(row):
                if mat[i][j] == 1:
                    if i > 0:
                        dp1[i][j] = dp1[i - 1][j] + 1
                    else:
                        dp1[i][j] = 1
                    width = 1
                    while len(dp) > 0 and dp[-1][0] >= dp1[i][j]:
                        pop_entry = dp.pop()
                        sum_val -= pop_entry[0] * pop_entry[1]
                        width += pop_entry[1]
                    sum_val += dp1[i][j] * width
                    dp.append([dp1[i][j], width])
                else:
                    dp = []
                    sum_val = 0
                ans += sum_val
        return ans
    
data = [[1,0,1],[1,1,0],[1,1,0]]
r = Solution().numSubmat(data)
print(r)