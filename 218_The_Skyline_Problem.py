from typing import List
from sortedcontainers import SortedList


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline = []
        right_arr = SortedList()
        for build in buildings:
            left, right, height = build[0], build[1], build[2]
            if len(skyline) == 0:
                skyline.append([left, height])
                right_arr.add([right, height])
            else:
                while len(right_arr) > 0 and right_arr[0][0] < left:
                    end_left = right_arr.pop(0)[0]
                    end_height = 0
                    if len(right_arr) > 0:
                        end_height = right_arr[0][1]
                    skyline.append([end_left, end_height])

                if skyline[-1][1] < height:
                    if skyline[-1][0] == left:
                        skyline[-1][1] = max(height, skyline[-1][1])
                    else:
                        skyline.append([left, height])

                idx = right_arr.bisect_right([right, height])
                if idx == len(right_arr) or right_arr[idx][1] <= height:
                    pop_idx = idx - 1
                    # print(right_arr, pop_idx)
                    while pop_idx >= 0 and right_arr[pop_idx][1] <= height:
                        right_arr.pop(pop_idx)
                        pop_idx -= 1
                    right_arr.add([right, height])
            # print(build, skyline, right_arr)

        while len(right_arr) > 0:
            end_left = right_arr.pop(0)[0]
            end_height = 0
            if len(right_arr) > 0:
                end_height = right_arr[0][1]
            skyline.append([end_left, end_height])
        return skyline


data = [[0,2,3],[2,5,3]]
# data = [[1,2,1],[1,2,2],[1,2,3]]
# data = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
r = Solution().getSkyline(data)
print(r)









