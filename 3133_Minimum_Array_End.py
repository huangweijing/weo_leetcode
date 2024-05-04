from collections import deque


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        binx, binn = list(bin(x)[2:]), list(bin(n - 1)[2:])
        ans = 0
        bit_cnt = 0
        while len(binx) > 0:
            b = binx.pop()
            if b == "1":
                ans += 1 << bit_cnt
            else:
                if len(binn) > 0:
                    ans += int(binn.pop()) << bit_cnt
            bit_cnt += 1
            # print(bin(ans))

        while len(binn) > 0:
            ans += int(binn.pop()) << bit_cnt
            bit_cnt += 1
            # print(bin(ans))
        return ans


r = Solution().minEnd(2, 7)
print(r)



