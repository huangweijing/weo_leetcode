from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        ans = 0
        cnt2 = Counter(word2)
        cnt1 = Counter(word1[: len(word2) - 1])
        left = 0
        for i, ch in enumerate(word1[len(word2) - 1: ], start=len(word2) - 1):
            cnt1[ch] += 1
            sub_okay = True
            for k, v in cnt2.items():
                if v > cnt1[k]:
                    sub_okay = False
                    break
            # print(cnt1, sub_okay, word1[left: i + 1])
            while sub_okay:
                ans += len(word1) - i
                cnt1[word1[left]] -= 1
                left += 1
                # print(len(word1) - i)
                for k, v in cnt2.items():
                    if v > cnt1[k]:
                        sub_okay = False
                        break
        return ans
    