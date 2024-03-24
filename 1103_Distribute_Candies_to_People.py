from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        i, c = 0, 1
        while candies > 0:
            if c > candies:
                c = candies
            candies -= c
            ans[i] += c
            c += 1
            i = (i + 1) % num_people
        return ans

r = Solution().distributeCandies(7, 4)
print(r)

