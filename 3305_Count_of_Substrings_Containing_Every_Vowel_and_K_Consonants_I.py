from collections import Counter


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel_cnt_arr = [0] * len(word)
        vowel_seq_cnt = 0
        for i in reversed(range(len(word))):
            ch = word[i]
            if ch in "aiueo":
                vowel_seq_cnt += 1
            else:
                vowel_seq_cnt = 0
            vowel_cnt_arr[i] = vowel_seq_cnt
        ans = 0
        cnt = Counter()
        conso_cnt = 0
        left = 0
        for i, ch in enumerate(word):
            # print(word[left: i + 1])
            if ch in "aiueo":
                cnt[ch] += 1
            else:
                conso_cnt += 1
            while conso_cnt > k:
                ch_left = word[left]
                if ch_left in "aiueo":
                    cnt[ch_left] -= 1
                    if cnt[ch_left] == 0:
                        del cnt[ch_left]
                else:
                    conso_cnt -= 1
                # print("deleting", word[left: i + 1])
                left += 1
            # print(i, cnt, conso_cnt)
            if len(cnt) == 5 and conso_cnt == k:
                # print("found!")
                ans += 1
                if i < len(word) - 1:
                    ans += vowel_cnt_arr[i + 1]
            while len(cnt) == 5 and conso_cnt == k:
                ch_left = word[left]
                if ch_left in "aiueo":
                    cnt[ch_left] -= 1
                    if cnt[ch_left] == 0:
                        del cnt[ch_left]
                else:
                    conso_cnt -= 1
                if len(cnt) == 5 and conso_cnt == k:
                    ans += 1
                    if i < len(word) - 1:
                        ans += vowel_cnt_arr[i + 1]
                left += 1
        return ans
    
data = [
    "ieaouqieaouqq"
    , 1
]
r = Solution().countOfSubstrings(*data)
print(r)
                