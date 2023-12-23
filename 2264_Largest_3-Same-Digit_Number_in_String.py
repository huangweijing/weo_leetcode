class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans_cn = ""
        i = 0
        while i < len(num):
            ch = num[i]
            cnt = 1
            while i < len(num) and num[i] == ch:
                i += 1
                cnt += 1
            if cnt > 3:
                ans_cn = max(ans_cn, ch)
        return ans_cn * 3


