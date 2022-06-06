class Solution:

    def say_num(self, s: str) -> str:
        idx = 0
        last_ch = None
        ch_cnt = 1
        result = ""
        while idx < len(s):
            ch = s[idx]
            # print(ch)
            if ch == last_ch:
                ch_cnt += 1
            else:
                if last_ch is not None:
                    result += str(ch_cnt) + last_ch
                    ch_cnt = 1
            last_ch = ch
            idx += 1

        if last_ch is not None:
            result += str(ch_cnt) + last_ch

        return result

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            pre_result = self.countAndSay(n - 1)
            return self.say_num(pre_result)

sol = Solution()
r = sol.countAndSay(30)
print(r)