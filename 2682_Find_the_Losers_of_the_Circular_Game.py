from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        received = set[int]([1])
        turn, current = 1, 1
        while True:
            current += turn * k
            current %= n
            if current == 0:
                current = n
            if current in received:
                break
            received.add(current)
            turn += 1

        ans = []
        for i in range(1, n + 1):
            if i not in received:
                ans.append(i)
        return ans

r = Solution().circularGameLosers(5, 3)
print(r)