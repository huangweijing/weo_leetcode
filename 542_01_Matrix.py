from typing import List

class Solution:
    def update_distance(self, point: list[int], distance_mat: list[list[int]]) -> List[List[int]]:
        m = len(distance_mat)
        n = len(distance_mat[0])
        row_idx = point[0]
        col_idx = point[1]
        updated_pos = list[list[int]]()
        if row_idx - 1 >= 0:
            if distance_mat[row_idx - 1][col_idx] == -1:
                distance_mat[row_idx - 1][col_idx] = \
                    distance_mat[row_idx][col_idx] + 1
                updated_pos.append([row_idx - 1, col_idx])
        if row_idx + 1 < m:
            if distance_mat[row_idx + 1][col_idx] == -1:
                distance_mat[row_idx + 1][col_idx] = \
                    distance_mat[row_idx][col_idx] + 1
                updated_pos.append([row_idx + 1, col_idx])
        if col_idx - 1 >= 0:
            if distance_mat[row_idx][col_idx - 1] == -1:
                distance_mat[row_idx][col_idx - 1] = \
                    distance_mat[row_idx][col_idx] + 1
                updated_pos.append([row_idx, col_idx - 1])
        if col_idx + 1 < n:
            if distance_mat[row_idx][col_idx + 1] == -1:
                distance_mat[row_idx][col_idx + 1] = \
                    distance_mat[row_idx][col_idx] + 1
                updated_pos.append([row_idx, col_idx + 1])
        return updated_pos


    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        distance_mat = [[-1] * n for i in range(m)]
        bfs_nl = list[list[int]]()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distance_mat[i][j] = 0
                    bfs_nl.append([i, j])
        while len(bfs_nl) > 0:
            new_bfs_nl = list[list[int]]()
            while len(bfs_nl):
                p = bfs_nl.pop()
                next_p = self.update_distance(p, distance_mat)
                new_bfs_nl.extend(next_p)
            bfs_nl = new_bfs_nl
        return distance_mat

r = Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]])
print(r)
