from typing import List

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]]
                       , pairs: List[List[int]]) -> int:
        pair_dict = {p[0]: p[1] for p in pairs} | {p[1]: p[0] for p in pairs}
        pref_dict = [{num: i for i, num in enumerate(p[1])} 
                     for p in enumerate(preferences)]
        # print(pref_dict)
        ans = 0
        for x in range(n):
            y = pair_dict[x]
            y_idx = pref_dict[x][y]
            for i in range(y_idx):
                u = preferences[x][i]
                v = pair_dict[u]
                x_idx = pref_dict[u][x]
                v_idx = pref_dict[u][v]
                if x_idx < v_idx:
                    ans += 1
                    # print(x, y, u, v)
                    break
        return ans

data = [
    4
    , [[1,2,3],[3,2,0],[3,1,0],[1,2,0]]
    , [[0,1],[2,3]]
]
r = Solution().unhappyFriends(*data)
print(r)
        