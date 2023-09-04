class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for i in range(low, high + 1):
            str_i = str(i)
            if len(str_i) & 1 == 1:
                continue
            if sum(map(int, str_i[:len(str_i) >> 1])) == \
                sum(map(int, str_i[len(str_i) >> 1: ])):
                ans += 1
        return ans
