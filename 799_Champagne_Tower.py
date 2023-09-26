class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        glass_tower = [[0] * (row_cnt + 1) for row_cnt in range(query_row + 1)]
        glass_tower[0][0] = poured
        for i in range(1, query_row + 1):
            for j in range(len(glass_tower[i])):
                if j - 1 >= 0 and glass_tower[i - 1][j - 1] > 1:
                    glass_tower[i][j] += (glass_tower[i - 1][j - 1] - 1) * 0.5
                if j < len(glass_tower[i - 1]) and glass_tower[i - 1][j] > 1:
                    glass_tower[i][j] += (glass_tower[i - 1][j] - 1) * 0.5
        return min(glass_tower[query_row][query_glass], 1)

data = [
6
, 2
, 1
]
r = Solution().champagneTower(* data)
print(r)