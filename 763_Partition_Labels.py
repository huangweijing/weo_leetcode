from typing import List
from collections import Counter

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt_head = set()
        ans = []
        partition_len = 0
        for i, ch in enumerate(s):
            cnt_head.add(ch)
            partition_len += 1
            if len(cnt_head.intersection(set(s[i + 1:]))) == 0:
                ans.append(partition_len)
                partition_len = 0
                cnt_head = set()
        return ans

r = Solution().partitionLabels("abccbaeef")
print(r)



