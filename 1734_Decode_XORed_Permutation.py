from typing import List
from functools import reduce


class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        ps = 0
        xor_no_1 = 0
        for e in encoded:
            ps = ps ^ e
            xor_no_1 ^= ps
        xor_all = reduce(lambda a, b: a ^ b, range(1, len(encoded) + 2))
        ans = [ xor_no_1 ^ xor_all ]
        for e in encoded:
            ans.append(ans[-1] ^ e)
        return ans
        