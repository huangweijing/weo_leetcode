from functools import cache
from collections import Counter

class Solution:

    def reorderedPowerOf2(self, n: int) -> bool:
        p2_arr = list[int]()
        n_str = str(n)
        max_int = 10 ** 9
        num = 1
        while num <= max_int:
            if len(n_str) == len(str(num)):
                p2_arr.append(num)
            elif len(n_str) < len(str(num)):
                break
            num <<= 1

        n_cnt = Counter(n_str)
        for p2 in p2_arr:
            p2_cnt = Counter(str(p2))
            if n_cnt == p2_cnt:
                return True
        return False

r = Solution().reorderedPowerOf2(4960)
print(r)