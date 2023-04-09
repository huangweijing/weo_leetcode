from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        zipped = list(map(lambda a: (a[0] - a[1], a[0], a[1]), zip(reward1, reward2)))
        zipped.sort(reverse=True, key=lambda a: a[0])
        ans = 0
        for i, item in enumerate(zipped):
            ans += item[1] if i < k else item[2]
        return ans



data = [
    [1,1,3,4]
    , [4,4,1,1]
    , 2
]
r = Solution().miceAndCheese(* data)
print(r)
