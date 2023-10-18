from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 1
        for num in target:
            while i < num:
                ans.append("Push")
                ans.append("Pop")
                i += 1
            if i == num:
                i += 1
                ans.append("Push")

        return ans

data = [
    [1,3]
    , 4
]
r = Solution().buildArray(* data)
print(r)

