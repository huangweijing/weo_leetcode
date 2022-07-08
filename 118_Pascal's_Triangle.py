from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, len(row) - 1):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]
            result.append(row)
        return result

r = Solution().generate(30)
print(r)