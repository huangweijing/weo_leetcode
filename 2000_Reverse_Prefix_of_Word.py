class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = -1
        appeared = False
        ch_stk = list[str]()
        for c in word:
            idx += 1
            ch_stk.append(c)
            if c == ch:
                appeared = True
                break
        if not appeared:
            return word
        ch_stk.reverse()
        return "".join(ch_stk) + word[idx + 1:]