class Solution:
    def minChanges(self, s: str) -> int:
        idx = 0
        ans = 0
        zero_cnt, one_cnt = 0, 0
        while idx < len(s):
            while idx < len(s) and s[idx] == "1":
                one_cnt += 1
                idx += 1
            if one_cnt & 1 == 1:
                ans += 1
                zero_cnt += 1
                one_cnt = 0
            while idx < len(s) and s[idx] == "0":
                zero_cnt += 1
                idx += 1
            if zero_cnt & 1 == 1:
                ans += 1
                one_cnt += 1
                zero_cnt = 0
        return ans

r = Solution().minChanges("11111000")
print(r)
