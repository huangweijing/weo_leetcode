from typing import List
from collections import Counter

class Solution:

    def hIndex(self, citations: List[int]) -> int:
        cnt = Counter(citations)
        key_list = list(cnt.keys())
        key_list.sort(reverse=True)
        acc_cnt = Counter()
        acc = 0
        for key in key_list:
            acc += cnt[key]
            acc_cnt[key] = acc
        # print(acc_cnt)
        key_list.sort()
        ans = 0
        for key in key_list:
            ans = max(ans, min(acc_cnt[key], key))
        return ans

data = [100]
r = Solution().hIndex(data)
print(r)