from typing import List
from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ch_cnt = Counter(chars)
        ans = 0
        for word in words:
            word_cnt = Counter(word)
            # print(word_cnt, ch_cnt)
            if word_cnt <= ch_cnt:
                ans += len(word)
        return ans

data = [
    ["cat","bt","hat","tree"]
    , "atach"
]
r = Solution().countCharacters(* data)
print(r)