class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        step = "c"
        for ch in word:
            if ch == "a":
                if step == "a":
                    ans += 2
                elif step == "b":
                    ans += 1
                step = "a"
            elif ch == "b":
                if step == "b":
                    ans += 2
                elif step == "c":
                    ans += 1
                step = "b"
            elif ch == "c":
                if step == "a":
                    ans += 1
                elif step == "c":
                    ans += 2
                step = "c"
        if step == "a":
            ans += 2
        elif step == "b":
            ans += 1
        return ans

data = "aaaabb"
r = Solution().addMinimum(data)
print(r)