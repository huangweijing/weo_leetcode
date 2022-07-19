import datetime


class Solution:
    def __init__(self):
        self.dp = dict[int, dict[int, int]]()
        # self.dp = [[None] * 1001 for i in range(1000001)]
        self.MODULO = 10 ** 9 + 7
        self.dig = [0] * 1001
        self.dig[1] = 1
        for i in range(2, len(self.dig)):
            self.dig[i] = self.dig[i - 1] + i - 1
        # print(self.dig)

    def k_my_inverse_pairs(self, n:int, k: int) -> int:
        if k < 0 or k >= self.dig[n]:
            return 0
        if n == 1:
            if k == 0:
                return 1
            else:
                return 0

        if n not in self.dp:
            self.dp[n] = dict[int, int]()
        if k in self.dp[n]:
            return self.dp[n][k]
        # mirror_k = self.dig[n] - 1 - k
        # if mirror_k <= 1000 and self.dp[n][mirror_k] is not None:
        #     self.dp[n][k] = self.dp[n][mirror_k]
        #     return self.dp[n][mirror_k]
        result = 0

        result = self.k_my_inverse_pairs(n, k - 1) + self.k_my_inverse_pairs(n - 1, k) \
            - self.k_my_inverse_pairs(n - 1, k - n)
        # for i in range(n):
        #     result += self.k_my_inverse_pairs(n - 1 , k - i) % self.MODULO
        self.dp[n][k] = result % self.MODULO

        # mirror_k = self.dig[n] - 1 - k
        # if mirror_k <= 1000 and self.dp[n][mirror_k] is not None:
        #     self.dp[n][mirror_k] = self.dp[n][k]
        return self.dp[n][k]

    def kInversePairs(self, n: int, k: int) -> int:
        # self.k_my_inverse_pairs(n, k)
        # self.dp[1][0] = 1
        for i in range(n + 1):
            for j in range(k + 1):
                self.k_my_inverse_pairs(i, j)
        return self.k_my_inverse_pairs(i, j)

t1 = datetime.datetime.now()
r = Solution().kInversePairs(1, 0)
t2 = datetime.datetime.now()
print(r, t2 - t1)
#
# for dn in range(6):
#     for dk in range(dn + 1):
#         print(f"{dn} \n"
#               f"{dk}")