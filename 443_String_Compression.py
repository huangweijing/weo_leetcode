from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        cur_ch = chars[0]
        ch_cnt = 0
        result = 0
        new_chars = []
        for i, ch in enumerate(chars):
            # print(ch, ch_cnt)
            if cur_ch == ch:
                ch_cnt += 1
            else:
                if ch_cnt == 1:
                    result += 1
                    new_chars.append(cur_ch)
                else:
                    new_chars.append(cur_ch)
                    new_chars.extend(list(str(ch_cnt)))
                    result += len(str(ch_cnt)) + 1
                cur_ch = ch
                ch_cnt = 1

        if ch_cnt == 1:
            result += 1
            new_chars.append(cur_ch)
        else:
            new_chars.append(cur_ch)
            new_chars.extend(list(str(ch_cnt)))
            result += len(str(ch_cnt)) + 1
        # print(new_chars)
        chars[: result] = new_chars
        return result

data = list("aaaaacaaaaaabbbbbbbbbbbbbbbbb")
r = Solution().compress(data)
print(r)
print(data)


