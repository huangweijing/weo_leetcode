from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        not_okay_set = set[int](range(len(strs)))
        i = 0
        while i < len(strs[0]):
            # print(not_okay_set)
            column_okay = True
            new_not_okay_set = set[int]()
            for j in not_okay_set:
                if j + 1 < len(strs) and strs[j][i] > strs[j + 1][i]:
                    column_okay = False
                    break
                elif j + 1 < len(strs) and strs[j][i] == strs[j + 1][i]:
                    new_not_okay_set.add(j)
                    # new_not_okay_set.add(j + 1)
            if not column_okay:
                ans += 1
            else:
                if len(new_not_okay_set) == 0:
                    return ans
                not_okay_set = new_not_okay_set
            i += 1
        return ans


data = ["xga","xfb","yfa"]
r = Solution().minDeletionSize(data)
print(r)

