from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        int_ch = 0
        op_idx = 0
        while k > 0:
            if k & 1 == 1:
                if operations[op_idx] == 1:
                    int_ch = int_ch + 1
            k >>= 1
            op_idx += 1
        ans = chr((int_ch % 26) + ord("a"))
        return ans
    

data = [
    10
    , [0,1,0,1]
]
r = Solution().kthCharacter(*data)
print(r)

        