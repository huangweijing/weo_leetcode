from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ch_cnt = Counter(s)
        stk = []
        for ch in s:
            ch_cnt[ch] -= 1
            if ch_cnt[ch] == 0:
                del ch_cnt[ch]
            if ch in stk:
                continue
            while len(stk) > 0 and stk[-1] > ch:
                if stk[-1] in ch_cnt:
                    stk.pop()
                else:
                    break
            stk.append(ch)

        return "".join(stk)

data = "cbacsalkdfowvzkjfahsdlfkhqwefkhasdflkjasdhfgasldflsawqeprasdfhkafdcbc"
r = Solution().removeDuplicateLetters(data)
print(r)



