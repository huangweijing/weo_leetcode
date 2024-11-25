from typing import List
from collections import defaultdict, Counter


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        dp = dict[int, Counter]()
        ans = 0
        for i in reversed(range(len(arr))):
            num1 = arr[i]
            if num1 not in dp:
                dp[num1] = Counter()
            for j in reversed(range(i)):
                num2 = arr[j]
                if num1 + num2 in dp and num1 in dp[num1 + num2]:
                    dp[num1][num2] = dp[num1 + num2][num1] + 1
                    ans = max(ans, dp[num1][num2])
                else:
                    dp[num1][num2] = 2
        return ans
    

data = [1,3,7,11,12,14,18]
r = Solution().lenLongestFibSubseq(data)
print(r)
                
