from typing import List


class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        sqr_list = []
        for i in range(2, 35):
            sqr_list.append(i ** 2)
        # print(sqr_list)
        sf = set()
        for num in nums:
            okay = 1
            for i in sqr_list:
                if i > num:
                    break
                if num % i == 0:
                    okay = 0
                    break
            if okay == 1:
                sf.add(num)

        return pow(2, len(sf), mod=10 ** 9 + 7) - 1


data = [
    [3,4,4,5]
]
r = Solution().squareFreeSubsets(* data)
print(r)

