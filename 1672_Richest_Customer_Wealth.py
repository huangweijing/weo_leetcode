from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for cust in accounts:
            result = max(result, sum(cust))
        return result