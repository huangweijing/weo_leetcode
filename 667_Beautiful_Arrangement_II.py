from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        direct = 0
        ans = []
        left, right = 1, n
        while k > 1:
            k -= 1
            if direct == 0:
                ans.append(left)
                left += 1
                direct = 1
            else:
                ans.append(right)
                right -= 1
                direct = 0
        if direct == 0:
            while len(ans) < n:
                ans.append(left)
                left += 1
        else:
            while len(ans) < n:
                ans.append(right)
                right -= 1
        return ans


r = Solution().constructArray(4, 3)
print(r)
