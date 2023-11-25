class Solution:
    def minimumSteps(self, s: str) -> int:
        okay_cnt = 0
        ans = 0
        for i, ch in enumerate(s):
            if ch == "0":
                ans += i - okay_cnt
                okay_cnt += 1
        return ans
