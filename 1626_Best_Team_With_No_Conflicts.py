from typing import List
from functools import cache

class Solution:
    def __init__(self):
        self.score_age = []

    @cache
    def my_sol(self, start_idx: int) -> int:
        if start_idx < 0:
            sa = (0, 0)
        else:
            sa = self.score_age[start_idx]
        idx = start_idx + 1
        stk = []
        max_score = 0
        while idx < len(self.score_age):
            if self.score_age[idx][0] >= sa[0] and self.score_age[idx][1] >= sa[1]:
                if len(stk) == 0:
                    stk.append(self.score_age[idx])
                    max_score = max(self.my_sol(idx), max_score)
                elif stk[-1][0] < self.score_age[idx][0] and stk[-1][1] > self.score_age[idx][1]:
                    stk.append(self.score_age[idx])
                    max_score = max(self.my_sol(idx), max_score)
            # if start_idx == 1:
            #     print("show: ", idx, stk, max_score)
            idx += 1
        # print(stk)
        ans = sa[0] + max_score
        # print(start_idx, ans)
        return ans

    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        self.score_age = list(zip(scores, ages))
        self.score_age.sort()
        # print(self.score_age)
        return self.my_sol(-1)


data = [
    [1,2,3,5]
    , [8,9,10,1]
]
r = Solution().bestTeamScore(* data)
print(r)