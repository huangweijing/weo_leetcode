from functools import cmp_to_key
from collections import Counter

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_arr = list(s)
        order_dict = Counter({ch : i for i, ch in enumerate(order)})
        s_arr.sort(key=cmp_to_key(lambda x, y: order_dict[x] - order_dict[y]))
        return "".join(s_arr)

data = [
    "abcdef"
    , "cccccccccdddddddaaag"
]
r = Solution().customSortString(* data)
print(r)