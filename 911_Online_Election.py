from typing import List
from collections import Counter
import bisect


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        person_time = zip(persons, times)
        cnt = Counter()
        self.p_arr, self.t_arr = [], []
        for p, t in person_time:
            cnt[p] += 1
            if len(self.p_arr) == 0 or cnt[self.p_arr[-1]] <= cnt[p]:
                self.p_arr.append(p)
            else:
                self.p_arr.append(self.p_arr[-1])
            self.t_arr.append(t)
        # print(self.p_arr, self.t_arr)

    def q(self, t: int) -> int:
        i = bisect.bisect_right(self.t_arr, t) - 1
        return self.p_arr[i]


data = [
    ["TopVotedCandidate","q","q","q","q","q","q"]
    , [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
]
ssa = TopVotedCandidate(*data[1][0])
result = []
for idx, command in enumerate(zip(data[0], data[1])):
    if idx == 0:
        continue
    ret = getattr(ssa, command[0])(* command[1])
    print(command[0], command[1], ret)
    result.append(ret)
print(result)