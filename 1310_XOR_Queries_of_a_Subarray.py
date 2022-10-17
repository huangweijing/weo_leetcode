from typing import List

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_sum = []
        xor_sum = 0
        for num in arr:
            xor_sum = num ^ xor_sum
            prefix_sum.append(xor_sum)

        ans = []
        for query in queries:
            if query[0] == 0:
                ans.append(prefix_sum[query[1]])
            else:
                ans.append(prefix_sum[query[1]] ^ prefix_sum[query[0] - 1])
        return ans

