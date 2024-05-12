from collections import Counter
import bisect
from typing import List


class Solution:
    def count_freq(self, word: str) -> int:
        cnt = Counter(word)
        min_ch = min(word)
        return cnt[min_ch]


    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freq_list = [self.count_freq(word) for word in words]
        freq_list.sort()
        # print(freq_list)
        return [len(words) - bisect.bisect_right(freq_list, self.count_freq(query)) for query in queries]


data = [
    ["bbb","cc"]
    , ["a","aa","aaa","aaaa"]
]
r = Solution().numSmallerByFrequency(*data)
print(r)