from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nlist = list(map(str, range(1, n + 1)))
        nlist.sort()
        return nlist

r = Solution().lexicalOrder(14)
print(r)
