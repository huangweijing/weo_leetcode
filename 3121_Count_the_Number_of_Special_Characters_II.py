from collections import Counter


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = Counter()
        not_special = set[int]()
        special_set = set[int]()
        for ch in word:
            if ch.lower() == ch and ch.upper() in cnt:
                not_special.add(ch)
            cnt[ch] += 1
        ans = 0
        for ch in cnt.keys():
            if ch == ch.lower():
                if ch in not_special:
                    continue
                if ch.upper() in cnt and ch not in special_set:
                    ans += 1
                    special_set.add(ch)
        return ans