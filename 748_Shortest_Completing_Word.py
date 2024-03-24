from typing import List
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate_cnt = Counter(licensePlate.lower())
        ans = "x" * 16
        for word in words:
            found_word = True
            word_cnt = Counter(word)
            for ch in range(ord("a"), ord("z") + 1):
                if chr(ch) in plate_cnt:
                    if chr(ch) not in word_cnt:
                        found_word = False
                        break
                    if word_cnt[chr(ch)] < plate_cnt[chr(ch)]:
                        found_word = False
                        break
            if found_word:
                if len(word) < len(ans):
                    ans = word
        return ans


data = [
"1s3 PSt"
, ["step","steps","stripe","stepple"]
]
r = Solution().shortestCompletingWord(* data)
print(r)