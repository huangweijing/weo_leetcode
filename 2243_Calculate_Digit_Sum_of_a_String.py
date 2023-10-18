import math


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ""
            for i in range(math.ceil(len(s) / k)):
                if (i + 1) * k <= len(s):
                    new_s += str(sum(map(int, s[i * k: (i + 1) * k])))
                else:
                    new_s += str(sum(map(int, s[i * k: ])))
            s = new_s
        return s


data = [
    "00000000"
    , 3
]
r = Solution().digitSum(*data)
print(r)
