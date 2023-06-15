from collections import Counter

class Solution:
    def minOperations(self, n: int) -> int:
        # print(bin(n))
        bin_str = list(reversed(bin(n)[2:]))
        # print(bin_str)
        one_cnt = 0
        ans = 0

        for i in range(len(bin_str)):
            ch = bin_str[i]
            # print(one_cnt)
            if ch == "1":
                one_cnt += 1
            else:
                if one_cnt == 1:
                    one_cnt = 0
                    ans += 1
                elif one_cnt > 1:
                    ans += 1
                    one_cnt = 1
        if one_cnt == 1:
            ans += 1
        elif one_cnt > 1:
            ans += 2
        return ans

r = Solution().minOperations(54)
print(r)

