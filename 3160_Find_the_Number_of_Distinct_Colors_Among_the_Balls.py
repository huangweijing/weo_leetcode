from typing import List
from collections import Counter


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_cnt = Counter()
        ball_color = Counter()
        ans = []
        for q in queries:
            if q[0] in ball_color:
                origin_color = ball_color[q[0]]
                color_cnt[origin_color] -= 1
                if color_cnt[origin_color] == 0:
                    del color_cnt[origin_color]
            color_cnt[q[1]] += 1
            ball_color[q[0]] = q[1]
            ans.append(len(color_cnt))
            # print(color_cnt, ball_color)
        return ans


data = [
    4
    , [[0,1],[1,2],[2,2],[3,4],[4,5]]
]
r = Solution().queryResults(* data)
print(r)


