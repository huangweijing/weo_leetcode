from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        template_word = []
        idx = 0
        while idx < len(s):
            ch = s[idx]
            ch_cnt = 0
            while idx < len(s) and s[idx] == ch:
                ch_cnt += 1
                idx += 1
            template_word.append([ch, ch_cnt])
        ans = 0
        for word in words:
            idx = 0
            tmp_idx = 0
            matched = True
            while idx < len(word):
                ch = word[idx]
                ch_cnt = 0
                while idx < len(word) and word[idx] == ch:
                    ch_cnt += 1
                    idx += 1
                if tmp_idx >= len(template_word):
                    matched = False
                    break
                tmp_entry = template_word[tmp_idx]
                # print(tmp_entry, ch, ch_cnt)
                if ch != tmp_entry[0] or tmp_entry[1] < ch_cnt:
                    matched = False
                    break
                if tmp_entry[1] < 3 and tmp_entry[1] != ch_cnt:
                    matched = False
                    break
                tmp_idx += 1
            if tmp_idx != len(template_word):
                matched = False
            if matched:
                # print(word)
                ans += 1
        return ans


data = [
    "heeeeeeeelloooooo"
    , ["hello", "heeeeello", "hell"]
]
r = Solution().expressiveWords(*data)
print(r)