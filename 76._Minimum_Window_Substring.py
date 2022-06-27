from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_hash = dict[str, int]()
        for ch in t:
            if ch in t_hash.keys():
                t_hash[ch] += 1
            else:
                t_hash[ch] = 1
        not_okay_ch_cnt = len(t_hash.keys())
        result: deque[str] = deque[str]()
        min_word = ""
        for idx, ch in enumerate(s):
            # print(s, t, t_hash, result)
            result.append(ch)
            if ch in t_hash.keys():
                t_hash[ch] -= 1
                if t_hash[ch] == 0 and not_okay_ch_cnt != 0:
                    not_okay_ch_cnt -= 1
            # pop out useless char
            while len(result) > 0:
                if result[0] not in t_hash.keys():
                    result.popleft()
                elif t_hash[result[0]] < 0:
                        t_hash[result[0]] += 1
                        result.popleft()
                else:
                    break

            if not_okay_ch_cnt == 0:
                # print("hey!")
                if min_word == "" or len(min_word) > len(result):
                    min_word = "".join(result)

        return min_word

sol = Solution()
r = sol.minWindow("ADOBECODEBANC", "ABC")
print(r)

