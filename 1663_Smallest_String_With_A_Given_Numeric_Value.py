class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        last_z_cnt = (k - n) // 25
        if last_z_cnt == n:
            return "z" * last_z_cnt

        last_not_z_ch = (k - n) % 25
        if last_not_z_ch == 0:
            return "a" * (n - last_z_cnt) + "z" * last_z_cnt
        else:
            return "a" * (n - last_z_cnt - 1) + \
                chr(ord("a") + last_not_z_ch) + \
                "z" * last_z_cnt


r = Solution().getSmallestString(9, 34)
print(r)

r = Solution().getSmallestString(5, 130)
print(r)

print("a" * 0)