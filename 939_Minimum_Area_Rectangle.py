from typing import List
import math


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_dict = dict[int, set[int]]()
        y_dict = dict[int, set[int]]()
        for point in points:
            if point[0] not in x_dict:
                x_dict[point[0]] = set[int]()
            x_dict[point[0]].add(point[1])

            if point[1] not in y_dict:
                y_dict[point[1]] = set[int]()
            y_dict[point[1]].add(point[0])

        ans = math.inf
        x_keys = sorted(list(x_dict.keys()))
        for i, x1 in enumerate(x_keys):
            y_set1 = x_dict[x1]
            if len(y_set1) < 2:
                continue
            for j in range(i + 1, len(x_keys)):
                x2 = x_keys[j]
                y_set2 = x_dict[x2]
                if len(y_set2) < 2:
                    continue
                node_set = y_set1 & y_set2
                if len(node_set) < 2:
                    continue
                node_list = sorted(list(node_set))
                for k in range(1, len(node_list)):
                    ans = min(ans, (node_list[k] - node_list[k - 1]) * (x2 - x1))
        if ans == math.inf:
            return 0
        return ans

data = [[0,1],[3,2],[5,5],[4,5],[4,4],[2,0],[2,3],[2,2],[1,0],[5,1],[2,5],[5,2],[2,4],[4,0]]

r = Solution().minAreaRect(data)
print(r)


