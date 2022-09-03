from typing import List

class Solution:
    def my_diff_seq(self, last_num: int, n:int, k:int) -> set[int]:
        result = set[int]()
        if n == 1:
            if last_num - k >= 0:
                result.add(last_num - k)
            if last_num + k <= 9:
                result.add(last_num + k)
            return result

        if last_num - k >= 0:
            highest_dig = (last_num - k) * (10 ** (n - 1))
            sub_result = self.my_diff_seq(last_num - k, n - 1, k)
            for sub in sub_result:
                result.add(highest_dig + sub)

        if last_num + k <= 9:
            highest_dig = (last_num + k) * (10 ** (n - 1))
            sub_result = self.my_diff_seq(last_num + k, n - 1, k)
            for sub in sub_result:
                result.add(highest_dig + sub)
        return result


    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = set[int]()
        for i in range(1, 10):
            pre_num = i * (10 ** (n - 1))
            sub_result = self.my_diff_seq(i, n - 1, k)
            for sub in sub_result:
                result.add(pre_num + sub)
        return list(result)

r = Solution().numsSameConsecDiff(2, 0)
print(r)

