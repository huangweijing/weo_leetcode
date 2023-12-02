from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        k = k % len(mat[0])
        for i, row in enumerate(mat):
            if i & 1 == 1:
                for j, col in enumerate(row):
                    # print(row[(j + k) % len(row)], col)
                    if row[(j + k) % len(row)] != col:
                        return False
            else:
                for j, col in enumerate(row):
                    # print(row[(j - k + len(row)) % len(row)], col)
                    if row[(j - k + len(row)) % len(row)] != col:
                        return False
        return True

data = [
    [[2,2],[4,5],[3,2],[4,6],[1,9],[5,3],[3,5],[2,4],[3,9]]
    , 7
    ]
r = Solution().areSimilar(*data)
print(r)