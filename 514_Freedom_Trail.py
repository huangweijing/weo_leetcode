from collections import defaultdict
import math


class Solution:
    def calc_cost(self, idx1: int, idx2: int, str_len: int):
        return min(abs(idx1 - idx2), str_len - abs(idx1 - idx2))

    def findRotateSteps(self, ring: str, key: str) -> int:
        char_dict = defaultdict(lambda : list[int]())
        for i, ch in enumerate(ring):
            char_dict[ch].append(i)

        last_cost = {0 : 0}
        for ch in key:
            idx_lst = char_dict[ch]
            new_cost = {idx: math.inf for idx in idx_lst}
            for idx in idx_lst:
                for last_idx, cost in last_cost.items():
                    new_cost[idx] = min(new_cost[idx]
                        , cost + self.calc_cost(idx, last_idx, len(ring)) + 1)
                    # print(idx, last_idx, new_cost, last_cost, self.calc_cost(idx, last_idx, len(ring)))
            # print("cost", last_cost, new_cost)
            last_cost = new_cost

        ans = math.inf
        for cost in last_cost.values():
            ans = min(ans, cost)
        return ans


print(Solution().calc_cost(7, 1, 8))


data = ["godding", "gd"]
r = Solution().findRotateSteps(* data)
print(r)



