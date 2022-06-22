from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        code_n_1: list[int] = self.grayCode(n - 1)
        code_n_1.extend(reversed(code_n_1))
        for i in range(len(code_n_1) >> 1):
            code_n_1[i] <<= 1
        for i in range(len(code_n_1) >> 1, len(code_n_1)):
            code_n_1[i] <<= 1
            code_n_1[i] += 1
        return code_n_1

r = Solution().grayCode(2)
print(r)

# data = [1, 2, 3]
# data.extend(reversed(data))
# print(data)
# for i in range(len(data) >> 1):
#     data[i] <<= 1
# for i in range(len(data) >> 1, len(data)):
#     data[i] <<= 1
#     data[i] += 1
# print(len(data) >> 1)
# print(data)