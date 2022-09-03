from typing import List
import bisect

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hm = dict()
        for item in items1:
            hm[item[0]] = hm.get(item[0], 0) + item[1]

        for item in items2:
            hm[item[0]] = hm.get(item[0], 0) + item[1]


        key_list = sorted(list(hm.keys()))
        return [[key, hm[key]] for key in key_list]

data_item1 = [[1,1],[4,5],[3,8]]
data_item2 = [[3,1],[1,5]]
r = Solution().mergeSimilarItems(data_item1, data_item2)
print(r)