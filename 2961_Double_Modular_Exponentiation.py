from typing import List


class Solution:

    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i, var in enumerate(variables):
            v1 = pow(base=var[0], exp=var[1], mod=10)
            v2 = pow(base=v1, exp=var[2], mod=var[3])
            if v2 == target:
                ans.append(i)
        return ans

