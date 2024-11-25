from typing import List
from collections import defaultdict


class Solution:
    def remainingMethods(self, n: int, k: int
                         , invocations: List[List[int]]) -> List[int]:
        call_from_dict = defaultdict(lambda: list[int]())
        call_dict = defaultdict(lambda: list[int]())
        for invoc in invocations:
            call_from_dict[invoc[1]].append(invoc[0])
            call_dict[invoc[0]].append(invoc[1])

        # print(call_from_dict)
        to_rem_set = {k}
        all_rem = set[int]()
        while len(to_rem_set) > 0:
            new_to_rem_set = set[int]()
            while len(to_rem_set) > 0:
                node = to_rem_set.pop()
                all_rem.add(node)
                next_call = call_dict[node]
                for call in next_call:
                    if call not in all_rem:
                        new_to_rem_set.add(call)
            to_rem_set = new_to_rem_set
            print(to_rem_set, all_rem)
        to_rem = set[int]()
        for call in range(n):
            call_from_list = call_from_dict[call]
            rem_flg = call in all_rem
            for call_from in call_from_list:
                if call_from not in all_rem:
                    rem_flg = False
                    break
            if rem_flg:
                to_rem.add(call)
        ans = set[int]()
        for i in range(n):
            if i not in to_rem:
                ans.add(i)
        return ans
        

data = [
    3
    , 2
    , [[1,0],[2,0]]
]
r = Solution().remainingMethods(*data)
print(r)