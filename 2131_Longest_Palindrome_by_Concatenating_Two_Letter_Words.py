from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_cnt = Counter()
        self_symmetric_word = Counter()
        ans = 0
        for word in words:
            if word[0] == word[1]:
                self_symmetric_word[word] += 1
            else:
                symmetric_word = word[::-1]
                if word_cnt[symmetric_word] > 0:
                    word_cnt[symmetric_word] -= 1
                    ans += 4
                else:
                    word_cnt[word] += 1
        # print(self_symmetric_word)
        has_single_one = False
        for val in self_symmetric_word.values():
            if val >= 2:
                ans += ((val >> 1) << 2)
            if val & 1 == 1:
                has_single_one = True
        if has_single_one:
            ans += 2
        return ans

data = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
r = Solution().longestPalindrome(data)
print(r)