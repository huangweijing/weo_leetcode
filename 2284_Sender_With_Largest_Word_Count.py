from typing import List
from collections import Counter


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        cnt = Counter()
        for i, message in enumerate(messages):
            arr = message.split()
            cnt[senders[i]] += len(arr)
        st = list(sorted(cnt.items(), key=lambda x: [x[1], x[0]]))
        return st[-1][0]