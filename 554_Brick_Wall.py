from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_cnt = dict[int, int]()
        max_edge_cnt = 0
        wall_sum = sum(wall[0])
        for row in wall:
            edge = 0
            for cell in row:
                edge += cell
                if edge == wall_sum:
                    break
                if edge not in edge_cnt:
                    edge_cnt[edge] = 0
                edge_cnt[edge] += 1
                if edge_cnt[edge] > max_edge_cnt:
                    max_edge_cnt = edge_cnt[edge]
        # print(edge_cnt)
        return len(wall) - max_edge_cnt


r = Solution().leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])
print(r)