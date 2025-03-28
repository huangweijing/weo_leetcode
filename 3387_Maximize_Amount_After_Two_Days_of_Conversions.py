from typing import List
from collections import defaultdict, deque


class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]]
    , rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        rate = defaultdict(lambda: dict[str, float]())
        for i, pair in enumerate(pairs1):
            rate[pair[0]][pair[1]] = rates1[i]
            rate[pair[1]][pair[0]] = 1 / rates1[i]
        max_cur = {key: 0 for key in rate.keys()}
        max_cur[initialCurrency] = 1.0

        cur_stk = deque([[initialCurrency, 1.0]])
        while len(cur_stk) > 0:
            cur = cur_stk.popleft()
            for new_cur, new_rate in rate[cur[0]].items():
                new_amount = cur[1] * new_rate
                if new_amount > max_cur[new_cur]:
                    max_cur[new_cur] = new_amount
                    cur_stk.append([new_cur, new_amount])
        # print(max_cur)
        rate = defaultdict(lambda: dict[str, float]())
        for i, pair in enumerate(pairs2):
            rate[pair[0]][pair[1]] = rates2[i]
            rate[pair[1]][pair[0]] = 1 / rates2[i]
        cur_stk = deque([[key, val] for key, val in max_cur.items()])
        while len(cur_stk) > 0:
            cur = cur_stk.popleft()
            for new_cur, new_rate in rate[cur[0]].items():
                new_amount = cur[1] * new_rate
                if new_cur not in max_cur:
                    max_cur[new_cur] = 0.0
                if new_amount > max_cur[new_cur]:
                    max_cur[new_cur] = new_amount
                    cur_stk.append([new_cur, new_amount])
        return max_cur[initialCurrency]
        
data = [
    "EUR"
    , [["EUR","USD"],["USD","JPY"]]
    , [2.0,3.0]
    , [["JPY","USD"],["USD","CHF"],["CHF","EUR"]]
    , [4.0,5.0,6.0]
]
r = Solution().maxAmount(*data)
print(r)

