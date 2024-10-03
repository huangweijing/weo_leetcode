from typing import List
from collections import Counter


class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        painting_dict = Counter()
        for seg in segments:
            painting_dict[seg[0]] += seg[2]
            painting_dict[seg[1]] -= seg[2]
        # print(painting_dict)
        color = 0
        key_list = list(sorted(painting_dict.keys()))
        ans = []
        for i, paint in enumerate(key_list[1:], start=1):
            color += painting_dict[key_list[i - 1]]
            if color > 0:
                ans.append([key_list[i - 1], key_list[i], color])
        return ans
    

data = [[1,7,9],[6,8,15],[8,10,7]]
r = Solution().splitPainting(data)
print(r)