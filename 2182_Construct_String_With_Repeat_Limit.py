from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        cnt = Counter(s)
        key_stk = []
        for ch in sorted(cnt.keys()):
            key_stk.append([ch, cnt[ch]])
        ans = ""
        last_sec = ["", 0]
        # print(key_stk)
        while len(key_stk) > 0:
            if key_stk[-1][0] == last_sec[0]:
                to_use = min(key_stk[-1][1], repeatLimit - last_sec[1])
                last_sec = [key_stk[-1][0], to_use + last_sec[1]]
            else:
                to_use = min(key_stk[-1][1], repeatLimit)
                last_sec = [key_stk[-1][0], to_use]
            key_stk[-1][1] -= to_use
            ans += key_stk[-1][0] * to_use
            
            if last_sec[1] == repeatLimit:
                if len(key_stk) > 1:
                    key_stk[-2][1] -= 1
                    ans += key_stk[-2][0]
                    last_sec = [key_stk[-2][0], 1]
                    if key_stk[-2][1] == 0:
                        tmp = key_stk.pop()
                        key_stk.pop()
                        key_stk.append(tmp)
                else:
                    break
            if len(key_stk) > 0 and key_stk[-1][1] == 0:
                key_stk.pop()
            # print(key_stk)
            # print(ans)
        return ans
    
data = [
"xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1
]
r = Solution().repeatLimitedString(*data)
print(r)