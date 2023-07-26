from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a_set, b_set, ans_set = set[int](), set[int](), set[int]()
        common = 0
        ans = []
        for i in range(len(A)):
            a_set.add(A[i])
            b_set.add(B[i])
            if A[i] in b_set and A[i] not in ans_set:
                common += 1
                ans_set.add(A[i])
            if B[i] in a_set and B[i] not in ans_set:
                common += 1
                ans_set.add(B[i])
            ans.append(common)
        return ans

data = [
    [2,3,1]
    , [3,1,2]
]
r = Solution().findThePrefixCommonArray(* data)
print(r)
