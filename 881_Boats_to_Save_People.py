from typing import List
from sortedcontainers import SortedDict
from collections import Counter

class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        sd = SortedDict(Counter(people))
        # print(sd)
        while len(sd) > 0:
            k, v, = sd.peekitem()
            if v == 1:
                sd.popitem()
            else:
                sd[k] = v - 1
            idx = sd.bisect_right(limit - k)
            # print(k, v, limit - k, sd, idx)
            if idx == 0:
                ans += 1
                continue
            pair_key, _ = sd.peekitem(idx - 1)
            # print(k, v, pair_key, sd)
            if sd[pair_key] == 1:
                del sd[pair_key]
            else:
                sd[pair_key] -= 1
            ans += 1
        return ans


r = Solution().numRescueBoats([2, 5, 5], 6)
print(r)


# sd = SortedDict()
# sd[3] = 5
# sd[12] = 0
# sd[9] = 12
# print(sd.bisect_right(3))