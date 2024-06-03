class Solution:
    def numSteps(self, s: str) -> int:
        zero_idx = [idx for idx, ch in enumerate(s) if ch == "0"]
        str_len = len(s)
        ans = 0
        while str_len > 1:
            # print(zero_idx, str_len)
            if len(zero_idx) > 0:
                idx = zero_idx.pop()
                if idx != str_len - 1:
                    ans += str_len - 1 - idx + 1
                    str_len = idx + 1
                else:
                    ans += 1
                    str_len -= 1
            elif len(zero_idx) == 0:
                ans += str_len + 1
                break
        return ans


r = Solution().numSteps("1001")
print(r)


