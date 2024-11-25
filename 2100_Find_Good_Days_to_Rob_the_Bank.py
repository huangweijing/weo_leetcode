from typing import List
from collections import deque


class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        non_inc_len, non_dec_len = [], deque()
        for i, sec in enumerate(security):
            if i > 0 and sec <= security[i - 1]:
                non_inc_len.append(non_inc_len[-1] + 1)
            else:
                non_inc_len.append(0)
        for i, sec in enumerate(reversed(security)):
            if i > 0 and sec <= security[-1 - i + 1]:
                non_dec_len.appendleft(non_dec_len[0] + 1)
            else:
                non_dec_len.appendleft(0)
        ans = []
        for i in range(time, len(security) - time):
            if non_inc_len[i] >= time and non_dec_len[i] >= time:
                ans.append(i)
        # print(non_inc_len, non_dec_len)
        return ans
    

data = [
    [5,3,3,3,5,6,2]
    , 2
]
r = Solution().goodDaysToRobBank(*data)
print(r)
