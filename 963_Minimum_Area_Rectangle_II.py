import math
from typing import List

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        vector_dict = dict[str, list[list[int]]]()
        vector_list = list[list[int]]()

        len_points = len(points)
        for i in range(len_points):
            for j in range(i + 1, len_points):
                p1, p2 = points[i], points[j]
                vector = [p1[0] - p2[0], p1[1] - p2[1]]
                vector_list.append(vector)
                key = f"{vector[0]}, {vector[1]}"
                key2 = f"{-vector[0]}, {-vector[1]}"
                if key not in vector_dict:
                    vector_dict[key] = list[list[int]]()
                if key2 not in vector_dict:
                    vector_dict[key2] = list[list[int]]()
                if p2[1] > p1[1]:
                    vector_dict[key].append([p1, p2])
                    vector_dict[key2].append([p1, p2])
                elif p2[1] < p1[1]:
                    vector_dict[key].append([p2, p1])
                    vector_dict[key2].append([p2, p1])
                elif p2[0] > p1[0]:
                    vector_dict[key].append([p1, p2])
                    vector_dict[key2].append([p1, p2])
                else:
                    vector_dict[key].append([p2, p1])
                    vector_dict[key2].append([p2, p1])
        # print(vector_dict)
        ans = math.inf
        for key, val in vector_dict.items():
            for i in range(len(val)):
                for j in range(i + 1, len(val)):
                    p1, p2 = val[i][0], val[i][1]
                    p3, p4 = val[j][0], val[j][1]
                    v1 = [p2[0] - p1[0], p2[1] - p1[1]]
                    v2 = [p3[0] - p1[0], p3[1] - p1[1]]
                    if v1[0] * v2[0] + v1[1] * v2[1] == 0:
                        # print(v1, v2, [p1, p2, p3, p4])
                        area = ((v1[0] ** 2 + v1[1] ** 2) ** 0.5) * ((v2[0] ** 2 + v2[1] ** 2) ** 0.5)
                        ans = min(area, ans)

        if ans == math.inf:
            return 0
        return ans

data = [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
r = Solution().minAreaFreeRect(data)
print(r)

