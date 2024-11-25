class Solution:
    def minFlips(self, s: str) -> int:
        dp1 = [0] * len(s)
        dp2 = dp1.copy()
        cost1, cost2 = 0, 0
        for i, ch in enumerate(s):
            if i == 0:
                dp1[i] = ch
                dp2[i] = "1" if ch == "0" else "1"
                cost2 += 1
            else:
                if ch == dp1[i - 1]:
                    dp1[i] = "1" if ch == "0" else "1"
                    cost1 += 1
                else:
                    dp1[i] = ch
                if ch == dp2[i - 1]:
                    dp2[i] = "1" if ch == "0" else "1"
                    cost2 += 1
                else:
                    dp2[i] = ch
        ans = min(cost1, cost2)
        for i in range(1, len(s)):
            # if dp1[i - 1] != dp1[]
            pass
