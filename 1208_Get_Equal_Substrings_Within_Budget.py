import bisect


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost_list = []
        cost = 0
        for i in range(len(s)):
            cost += abs(ord(s[i]) - ord(t[i]))
            cost_list.append(cost)
        # print(cost_list)
        cost = 0
        ans = 0
        for i in range(len(s)):
            idx = bisect.bisect_right(cost_list, cost + maxCost) - 1
            ans = max(idx + 1 - i, ans)
            cost += abs(ord(s[i]) - ord(t[i]))
        return ans


data = [
    "abcd"
    , "cdef"
    , 3
]
r = Solution().equalSubstring(* data)
print(r)