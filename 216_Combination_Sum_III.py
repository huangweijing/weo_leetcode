from typing import List

class Solution:
    def __init__(self):
        #k, n
        self.dp = [[None] * 61 for i in range(10)]

    def gen_key(self, num_set: set[int]) -> str:
        num_list = list(num_set)
        num_list.sort()
        key = ""
        for num in num_list:
            key += str(num)
        return key

    def my_comb(self, k: int, n: int) -> list[set[int]]:
        if n <= 0 or k <= 0:
            return None
        # print(k, n)
        result = []
        if k == 1:
            if n > 9:
                return None
            else:
                result.append({n})

        if self.dp[k][n] is not None:
            return self.dp[k][n]

        result_key_set = set[str]()
        for i in range(1, 10):
            num_set_list = self.my_comb(k - 1, n - i)
            if num_set_list is None:
                continue
            num_set_list = num_set_list.copy()
            for num_set in num_set_list:
                if i in num_set:
                    continue
                num_set = num_set.copy()
                num_set.add(i)
                key = self.gen_key(num_set)
                if key not in result_key_set:
                    result.append(num_set)
                    result_key_set.add(key)
        self.dp[k][n] = result
        return result

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = list[list[int]]()
        set_list = self.my_comb(k, n)
        for s in set_list:
            result.append(list(s))
        return result

r = Solution().combinationSum3(3, 9)
print(r)


