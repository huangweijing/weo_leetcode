class Solution:
    def countTime(self, time: str) -> int:
        ans = 1
        if time[:2] == "??":
            ans *= 24
        elif time[0] == "?":
            if time[1] >= "4":
                ans *= 2
            else:
                ans *= 3
        elif time[1] == "?":
            if time[0] == "2":
                ans *= 4
            else:
                ans *= 10
        if time[3] == "?":
            ans *= 6
        if time[4] == "?":
            ans *= 10
        return ans

r = Solution().countTime("?5:??")
print(r)
