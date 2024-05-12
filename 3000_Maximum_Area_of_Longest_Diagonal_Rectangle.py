from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        ans = 0
        for dim in dimensions:
            diagonal = (dim[0] ** 2 + dim[1] ** 2) ** 0.5
            if diagonal > max_diagonal:
                max_diagonal = diagonal
                ans = dim[0] * dim[1]
            elif diagonal == max_diagonal:
                ans = max(dim[0] * dim[1], ans)
        return ans


data = [[6,5],[8,6],[2,10],[8,1],[9,2],[3,5],[3,5]]
r = Solution().areaOfMaxDiagonal(data)
print(r)
