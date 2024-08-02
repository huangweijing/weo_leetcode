from typing import List
import math

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [[math.inf, math.inf] for _ in range(shelfWidth + 1)]
        dp[0] = [0, 0]
        for book in books:
            new_dp = [[math.inf, math.inf] for _ in range(shelfWidth + 1)]
            for i, entry in enumerate(dp):
                if entry[0] == math.inf:
                    continue
                # print("entry", entry)
                new_entry = [entry[0] - entry[1] + max(book[1], entry[1]), max(book[1], entry[1])]
                if i + book[0] <= shelfWidth and new_entry < new_dp[i + book[0]]:
                    new_dp[i + book[0]] = new_entry
                new_entry = [entry[0] + book[1], book[1]]
                if new_entry < new_dp[book[0]]:
                    new_dp[book[0]] = new_entry
            dp = new_dp
            # print("dp", dp)
        ans = math.inf
        for entry in dp:
            ans = min(entry[0], ans)
        return ans


data = [
    [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
    , 4
]
r = Solution().minHeightShelves(*data)
print(r)


