class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        space_cnt = 0
        idx = -1
        for i, ch in enumerate(s):
            if ch == " ":
                space_cnt += 1
            if space_cnt == k:
                idx = i
                break
        if space_cnt < k:
            return s
        return s[: idx]