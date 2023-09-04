from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        ans = [["."] * m for _ in range(n)]

        for i, row in enumerate(box):
            stone_cnt = 0
            for j, item in enumerate(row):
                if item == "*":
                    ans[j][i] = "*"
                    while stone_cnt > 0:
                        ans[j - stone_cnt][i] = "#"
                        stone_cnt -= 1
                elif item == "#":
                    stone_cnt += 1
            while stone_cnt > 0:
                ans[n - stone_cnt][i] = "#"
                stone_cnt -= 1

        for i in range(n):
            row = ans[i]
            for j in range(m):
                if row[j] != "*" and row[j] != "#":
                    row[j] = "."
                if m - 1 - j > j:
                    row[m - 1 - j], row[j] = row[j], row[m - 1 - j]
        return ans


data = [["#",".","*","."],["#","#","*","."]]
r = Solution().rotateTheBox(data)
print(r)