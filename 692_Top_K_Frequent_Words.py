from typing import List
from collections import Counter
from sortedcontainers import SortedList, SortedDict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        val_dict = SortedDict()
        for key, val in cnt.items():
            if val not in val_dict:
                val_dict[val] = SortedList()
            val_dict[val].add(key)

        ans = []
        for val, l in reversed(val_dict.items()):
            if len(l) < k:
                ans.extend(l)
                k -= len(l)
            else:
                ans.extend(l[:k])
                break
        return ans

data = [
    ["i","love","leetcode","i","love","coding", "coding"]
    ,2
]
r = Solution().topKFrequent(* data)
print(r)