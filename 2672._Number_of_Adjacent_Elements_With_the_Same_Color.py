from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        adj_same_cnt = 0
        arr = [0] * n
        for query in queries:
            idx = query[0]
            color = query[1]
            old_color = arr[idx]
            if color == old_color:
                ans.append(adj_same_cnt)
            elif color != 0:
                if old_color != 0:
                    if idx + 1 < len(arr) and old_color == arr[idx + 1]:
                        adj_same_cnt -= 1
                    if idx > 0 and old_color == arr[idx - 1]:
                        adj_same_cnt -= 1
                if idx + 1 < len(arr) and color == arr[idx + 1]:
                    adj_same_cnt += 1
                if idx > 0 and color == arr[idx - 1]:
                    adj_same_cnt += 1
                arr[idx] = color
                ans.append(adj_same_cnt)
        return ans


data = [
    4
    , [[0,2],[1,2],[3,1],[1,1],[2,1]]
]
r = Solution().colorTheArray(* data)
print(r)
