from typing import List
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        bin_list = list(map(int, bin(n)[2:]))
        powers, bit_idx = [], 0
        while len(bin_list) > 0:
            if bin_list.pop() == 1:
                powers.append(bit_idx)
            bit_idx += 1
        prefix_product_arr, prefix_product = [], 0
        for power in powers:
            prefix_product += power
            prefix_product_arr.append(prefix_product)
        ans = []
        for query in queries:
            if query[0] == 0:
                ans.append(prefix_product_arr[query[1]])
            else:
                ans.append(prefix_product_arr[query[1]] - prefix_product_arr[query[0] - 1])
        ans = list(map(lambda x: (2 ** x) % (10 ** 9 + 7), ans))
        return ans


data = [
    15
    , [[0,1],[2,2],[0,3]]
]
r = Solution().productQueries(*data)
print(r)
