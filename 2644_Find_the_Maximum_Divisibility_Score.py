from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_score = 0
        ans = 99999999999
        for div in divisors:
            score = 0
            for num in nums:
                if num % div == 0:
                    score += 1
            if score > max_score:
                ans = 99999999999
                max_score = score
            if score == max_score:
                ans = min(ans, div)
        return ans

data = [
    [12]
    , [10, 16]
]
r = Solution().maxDivScore(* data)
print(r)