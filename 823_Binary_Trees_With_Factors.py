from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        # initialize
        arr.sort()
        fbt = dict[int, int]()
        mult_link = dict[int, list[list[int]]]()
        for num in arr:
            fbt[num] = 1
            mult_link[num] = list[list[int]]()

        # link
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                # print(i, j)
                if arr[i] * arr[j] in fbt:
                    mult_link[arr[i] * arr[j]].append([arr[i], arr[j]])

        # update
        for num in arr:
            while len(mult_link[num]) > 0:
                p = mult_link[num].pop()
                i, j = p[0], p[1]
                if i == j:
                    fbt[num] += (fbt[i] ** 2)
                else:
                    fbt[num] += (fbt[i] * fbt[j]) * 2

        result = 0
        for key in fbt:
            result += fbt[key]
        # print(fbt)
        return result % (10 ** 9 + 7)

r = Solution().numFactoredBinaryTrees([2,4,5,8,10,20])
print(r)




