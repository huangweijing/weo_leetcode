from typing import List

class Solution:
    def my_combine(self, num_list: list[int], k: int) -> list[list[int]]:
        if k == 1:
            return [[i] for i in num_list]
        else:
            result = list[list[int]]()
            for i in range(len(num_list)):
                my_comb_n_1 = self.my_combine(num_list[i + 1:], k - 1)
                my_comb_n_1 = my_comb_n_1.copy()
                for my_comb in my_comb_n_1:
                    my_comb.append(num_list[i])
                    result.append(my_comb)
            return result


    def combine(self, n: int, k: int) -> List[List[int]]:
        result = self.my_combine(list(range(1, n + 1)), k)
        return result


sol = Solution()
r = sol.combine(4, 2)
print(r)
