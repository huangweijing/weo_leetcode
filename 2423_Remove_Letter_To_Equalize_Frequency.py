from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        alp_freq = Counter(word)
        freq_cnt = Counter(alp_freq.values())
        # aaaa
        if len(alp_freq) == 1:
            return True
        # abcd
        if len(freq_cnt) == 1 and max(freq_cnt.keys()) == 1:
            return True
        # aaac
        if len(freq_cnt) == 2 and freq_cnt[1] == 1:
            return True
        # aaaabbbccc
        if len(freq_cnt) == 2 \
            and max(freq_cnt.keys()) == min(freq_cnt.keys()) + 1 \
            and freq_cnt[max(freq_cnt.keys())] == 1:
            return True
        return False


r = Solution().equalFrequency("abcc")
print(r)