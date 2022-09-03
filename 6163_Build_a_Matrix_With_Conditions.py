from typing import List
import functools

class MyCmp:
    def __init__(self, conditions: list[list[int]]):
        self.conditions = conditions
        self.comp_map = dict[int, int]()
        for cond in self.conditions:
            key1 = cond[0] * 500 + cond[1]
            self.comp_map[key1] = -1
            key2 = cond[1] * 500 + cond[0]
            self.comp_map[key2] = 1
            print(cond[0], cond[1], -1)
        print(self.comp_map)

    def cmpare(self, o1:int, o2:int):
        # return o2 - o1
        return self.comp_map.get(o1 * 500 + o2, o1 - o2)

class Solution:

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        my_cmp_row = MyCmp(rowConditions)
        row_rank = list(range(1, k + 1))
        row_rank.sort(key=functools.cmp_to_key(my_cmp_row.cmpare))

        my_cmp_col = MyCmp(colConditions)
        col_rank = list(range(1, k + 1))
        col_rank.sort(key=functools.cmp_to_key(my_cmp_col.cmpare))

        point_list = [[0] * 2 for i in range(k + 1)]
        for i in range(len(row_rank)):
            point_list[row_rank[i]][0] = i

        for i in range(len(col_rank)):
            point_list[row_rank[i]][1] = i

        matrix = [[0] * k for i in range(k)]
        for pidx in range(1, len(point_list)):
            matrix[point_list[pidx][0]][point_list[pidx][1]] = pidx
        return matrix



r = Solution().buildMatrix(3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]])
print(r)