from typing import List
from collections import Counter


class Solution:
    def __init__(self) -> None:
        self.num_cnt = Counter()
        self.key_arr = []

    def my_sol(self, key_idx: int, target: int) -> list[list[int]]:
        if key_idx == len(self.key_arr):
            return None
        ret = []
        key = self.key_arr[key_idx]
        for j in range(0, self.num_cnt[key] + 1):
            if key * j > target:
                break
            to_append = [key] * j
            if target - key * j == 0:
                ret.append(to_append)
            else:
                sub_sol = self.my_sol(key_idx + 1, target - key * j)
                if sub_sol is None or len(sub_sol) == 0:
                    continue
                for sub in sub_sol:
                    sub.extend(to_append)
                    ret.append(sub)
        return ret

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.num_cnt = Counter(candidates)
        self.key_arr = list(sorted(self.num_cnt.keys()))
        # print(self.num_cnt, self.key_arr)
        return self.my_sol(0, target)


data = [
    [10,1,2,7,6,1,5]
    , 8
]
r = Solution().combinationSum2(*data)
print(r)