from typing import List

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        row_cnt = len(heightMap)
        col_cnt = len(heightMap[0])
        max_from_left = [[0] * col_cnt for i in range(row_cnt)]
        max_from_right = [[0] * col_cnt for i in range(row_cnt)]
        max_from_up = [[0] * col_cnt for i in range(row_cnt)]
        max_from_down = [[0] * col_cnt for i in range(row_cnt)]

        for idx in range(row_cnt):
            max_left = -1
            max_right = -1
            idx2 = 0
            while idx2 < len(col_cnt):
                if max_left < heightMap[idx][idx2]:
                    max_left = heightMap[idx][idx2]
                max_from_left[idx][idx2] = max_left
                idx2 += 1
            idx2 = len(col_cnt) - 1
            while idx2 >= 0:
                if max_right < heightMap[idx][idx2]:
                    max_right = heightMap[idx][idx2]
                max_from_right[idx][idx2] = max_left
                idx2 += 1