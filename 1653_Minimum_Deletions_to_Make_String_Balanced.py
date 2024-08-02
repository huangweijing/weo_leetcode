class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt_right = 0
        cnt_left = 0
        for ch in s:
            if ch == "a":
                cnt_right += 1
        ans = cnt_right
        for ch in s:
            if ch == "a":
                cnt_right -= 1
            else:
                cnt_left += 1
            ans = min(ans, cnt_right + cnt_left)
        return ans
