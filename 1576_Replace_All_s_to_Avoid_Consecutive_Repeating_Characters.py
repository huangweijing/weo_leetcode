class Solution:
    def modifyString(self, s: str) -> str:
        ans = ""
        for i, ch in enumerate(s):
            if ch != "?":
                ans += ch
            else:
                ban_set = set[str]()
                if i > 0:
                    ban_set.add(ans[i - 1])
                if i < len(s) - 1:
                    ban_set.add(s[i + 1])
                append_ch = ""
                for c in range(ord("a"), ord("z") + 1):
                    if chr(c) not in ban_set:
                        append_ch = chr(c)
                        break
                ans += append_ch
        return ans

