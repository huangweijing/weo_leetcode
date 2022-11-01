from typing import List
from collections import deque, defaultdict

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        pair_dict = defaultdict(lambda : [])
        for pair in adjacentPairs:
            pair_dict[pair[0]].append(pair[1])
            pair_dict[pair[1]].append(pair[0])

        ans = deque()
        ans.append(adjacentPairs[0][0])
        ans.append(adjacentPairs[0][1])
        # print(ans, pair_dict)
        while len(ans) < len(adjacentPairs) + 1:
            if ans[-1] in pair_dict:
                pair = pair_dict[ans[-1]]
                if len(pair) == 1:
                    if pair[0] != ans[-2]:
                        ans.append(pair[0])
                else:
                    n1, n2 = pair
                    ans.append(n1 if n2 == ans[-2] else n2)

            if ans[0] in pair_dict:
                pair = pair_dict[ans[0]]
                if len(pair) == 1:
                    if pair[0] != ans[1]:
                        ans.appendleft(pair[0])
                else:
                    n1, n2 = pair_dict[ans[0]]
                    ans.appendleft(n1 if n2 == ans[1] else n2)
            # print(ans)

        return list(ans)

data = [[100000,-100000]]
r = Solution().restoreArray(data)
print(r)

